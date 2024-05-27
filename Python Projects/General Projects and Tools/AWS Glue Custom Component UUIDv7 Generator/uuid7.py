from awsglue import DynamicFrame
from pyspark.sql.functions import udf # user defined function
from pyspark.sql.types import StringType
from awsglue.dynamicframe import DynamicFrame
import uuid6

def create_UUIDv7 (self,column_name='id'):
    """Adds a new column with UUIDv7 values to the DynamicFrame."""
    
    data_frame = self.toDF()
    
    # create a function that generates a new UUIDv7
    uuid7_generator: udf = udf(lambda: str(uuid6.uuid7()), StringType())
    
    # add a new uuid column
    new_data_frame = data_frame.withColumn(column_name, uuid7_generator())
    
    # convert the data frame to a dynamic frame
    new_dynamic_frame: DynamicFrame = DynamicFrame.fromDF(new_data_frame, self.glue_ctx, "with_converted_id")
    
    # return the updated dynamic frame
    return new_dynamic_frame

DynamicFrame.create_UUIDv7 = create_UUIDv7