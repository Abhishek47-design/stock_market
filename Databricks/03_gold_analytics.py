# Databricks notebook source
from pyspark.sql.functions import *

gold_df = (
    spark.table("silver_stock_stream")
    .groupBy("symbol")
    .agg(
        round(avg("current_price"),2).alias("avg_price"),
        round(max("current_price"),2).alias("max_price"),
        round(min("current_price"),2).alias("min_price"),
        round(stddev("current_price"),2).alias("volatility"),
        count("*").alias("record_count")
    )
)

gold_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("gold_stock_stream")

print("Gold Layer Created")

# COMMAND ----------

