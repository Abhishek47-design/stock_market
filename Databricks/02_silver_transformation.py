# Databricks notebook source
from pyspark.sql.functions import *

silver_df = (
    spark.table("bronze_stock_stream_final")
    .dropDuplicates()
    .dropna()
    .withColumn(
        "event_timestamp",
        to_timestamp("timestamp")
    )
    .withColumn(
        "ingestion_timestamp",
        current_timestamp()
    )
)

silver_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver_stock_stream")

print("Silver Layer Created")

# COMMAND ----------

