
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
