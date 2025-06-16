from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import udf, col, concat_ws
from pyspark.sql.types import StringType
import uuid6
from datetime import datetime, timedelta

import boto3
import base64,json, psycopg2



# Constants ====================================================

# daily_etl forced date 
forced_date = None          # default case, take current_date
# forced_date = '2024-11-18'  # use if you want to force a date for the migration group

# %connection _connection_name_
# glueContext.create_dynamic_frame( _glue_database_name_ )

legacy_connection = {
    # domain:       _glue_database_name_
}

# env_migrate, env_prod, env_staging, env_test
env_connection = {
    # domain:       _glue_database_name_
}

years = '(2025)'
m_groups = ("Test Group A","Test Group A")


# these 2 dictionaries are to get the database credentials for the databases from AWS Secret Manager
secret_names = {
    # database:       AWS Secret Name
}

db_hosts = {
    # database:       db_host
}

# Functions ==================================================== 
db_mapping = {
    # env:          database
}


def sparkSqlQuery_(query, mapping, glueContext = None, ctx = ''):
    if glueContext is None:
        raise ValueError("glueContext must be provided")
    for alias, frame in mapping.items():
        try:
            frame.toDF().createOrReplaceTempView(alias)
        except:
            print(f'ERROR sparkSqlQuery:\n{alias} is mapped to a non-DynamicFrame: {frame}\n')
    result = glueContext.spark_session.sql(query)
    return DynamicFrame.fromDF(result, glueContext, ctx)

def generate_uuid():
    return str(uuid6.uuid7())

uuid_udf = udf(generate_uuid, StringType())

def add_field_(dynamicFrame, name = 'id', value = uuid_udf, glueContext = None):
    if glueContext is None:
        raise ValueError("glueContext must be provided")
    
    temp_df = dynamicFrame.toDF().withColumn(name, value())
    final_df = DynamicFrame.fromDF(temp_df, glueContext, dynamicFrame.name)
    return sparkSqlQuery_(f'SELECT * FROM df ORDER BY {name}', {"df": final_df}, glueContext)


def read_table_(env, table, glueContext = None):
    if glueContext is None:
        raise ValueError("glueContext must be provided")
    
    db = db_mapping.get(env, "ERROR")
    if db == "ERROR":
        print(f"Invalid Environment: {env}")
        return None
    try:
        if env == "bigquery":
            return glueContext.create_dynamic_frame.from_options(
                connection_type = env,
                connection_options = {
                    "connectionName": env,
                    "parentProject": db,
                    "table": table,
                    "viewsEnabled": "true"
                })
        else:
            return glueContext.create_dynamic_frame.from_catalog(
                database = env,
                table_name = f"{db}_{table}")
    except Exception as e:
        raise ValueError(f'ERROR when reading {table} from {env}:\n\n{e}')



def write_table_(frame, env, table, glueContext = None):
    current_time = datetime.now() - timedelta(hours=6)
    if glueContext is None:
        raise ValueError("glueContext must be provided")
    
    db = db_mapping.get(env, "ERROR")
    if db == "ERROR":
        print(f"Invalid Environment: {env}")
        return
    try:
        # read the target table:
        target_df = read_table_(env,table,glueContext).toDF()
        source_df = frame.toDF()
        print(f'Target table: {env}.{table}')
        # compare columns 
        target_columns = set(target_df.columns)
        source_columns = set(source_df.columns)
        if target_columns == source_columns:
            print('✅ Target columns match the source columns. No difference found\n')
        else:
            print(f'❓Target columns do not match the source!\nMissing columns from the source: {list(target_columns-source_columns)}\nExtra columns in the source: {list(source_columns-target_columns)}\n')
        rows = source_df.count()
        if rows > 0:
            glueContext.write_dynamic_frame.from_catalog(
                frame = frame,
                database = env,
                table_name = f"{db}_{table}"
            )
            print(f'{current_time}\n{rows} rows have been migrated successfully!')
        else:
            print(f'No rows to migrate for {env}.{table}')
    except Exception as e:
        # print(f'ERROR: {e}')
        raise ValueError(f'ERROR when writing {table} to {env}: (maybe a null column?)\n\n {e}')
    print("\033[91m" + '=' * 80 + "\033[0m") # red double line


def write_csv(frame, path='ledger/', mode="overwrite"):
    # make sure that the path is correct 
    if path[0] =='/':
        path = path[1:]
    if path[-1] != '/':
        path = path + '/'
    df = frame.toDF()
    
    # convert array columns to string
    for field in df.schema.fields:
        if "array" in str(field.dataType):
            df = df.withColumn(field.name, concat_ws(",", col(field.name)))
            
    output_path = 's3://s3_bucket/notebooks/results/' + path
    output_url = f'https://region.console.aws.amazon.com/s3/buckets/s3_bucket?region=region&bucketType=general&prefix=notebooks/results/{path}&showversions=false'
    # Extract bucket name and prefix from S3 path
    s3 = boto3.client("s3")
    bucket, prefix = output_path.replace("s3://", "").split("/", 1)
    # List existing files in the S3 directory
    response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
    
    if "Contents" in response:
        existing_files = [obj["Key"] for obj in response["Contents"]]
        # Check if any non-CSV files exist
        non_csv_files = [f for f in existing_files if not f.endswith(".csv")]
        if non_csv_files:
            # print(f"Non-CSV files detected in {output_path}: {non_csv_files}")
            raise Exception(f"\n❌ Non-CSV files detected in {output_path}: {non_csv_files}\nChange path and try again!")

    # Write the DataFrame to S3 as CSV

    df.coalesce(1).write.csv(
        path=output_path,
        header=True,
        mode=mode
    )
    print(f"✅ Successfully written CSV to {output_path}\n\nCheck here: (open in new tab or copy URL to browser)\n{output_url}")

def get_secret(secret_name, region_name):
    # Create a Secrets Manager client
    client = boto3.client('secretsmanager', region_name=region_name)

    try:
        # Retrieve the secret value
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        
        # Decrypts secret using the associated KMS key
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            secret = base64.b64decode(get_secret_value_response['SecretBinary'])

        # Convert secret to JSON if it's in JSON format
        secret_dict = json.loads(secret)
        return secret_dict

    except Exception as e:
        print(f"Error retrieving secret: {e}")
        raise e
    
def connect_to_db(database = 'env_migrate',region_name = "region"):
    try:
        # get the secret from AWS secrets
        secret_name = secret_names[database]
        secret = get_secret(secret_name, region_name)
        # try to retrieve info
        db_host = db_hosts[database]
        db_port = 5432
        db_name = db_mapping[database]
        db_user = secret['username']
        db_password = secret['password']
    except Exception as e:
        print(f"Error retrieving secret: {e}")
        raise e
        
    try:
        # try to connect to db
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        print(f'Connected to {database}\n')
        print('Do not forget to close the connection using\nconn.close()')
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise e
    
    
    



