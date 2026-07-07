from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as sum_

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("BigQuery Read") \
    .getOrCreate()

# Replace with your BigQuery dataset and table name
dataset_id = "superb-shelter-403306.CUSTOMER_DB"
table_id = "superb-shelter-403306.CUSTOMER_DB.gadgets_order_data"

# Read data from BigQuery
df = spark.read \
    .format("bigquery") \
    .option("dataset", dataset_id) \
    .option("table", table_id) \
    .load()

# Calculate total sales as quantity * price
df = df.withColumn("total_sales", col("quantity") * col("price"))

# Group by item and sum total sales
result_df = df.groupBy("item").agg(sum_("total_sales").alias("sum_total_sales"))

# Show the result
result_df.show()

# Stop the SparkSession
spark.stop()