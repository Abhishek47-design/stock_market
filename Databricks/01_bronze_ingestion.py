# Databricks notebook source
source_path = "/Volumes/workspace/default/stock_market/"

schema_path = "/Volumes/workspace/default/stock_market_source/schema"

checkpoint_path = "/Volumes/workspace/default/stock_market_source/checkpoint"

sample_df = spark.read.json(source_path)

schema = sample_df.schema

stream_df = (
    spark.readStream
         .format("cloudFiles")
         .option("cloudFiles.format", "json")
         .option(
             "cloudFiles.schemaLocation",
             schema_path
         )
         .schema(schema)
         .load(source_path)
)

(
    stream_df.writeStream
        .format("delta")
        .option(
            "checkpointLocation",
            checkpoint_path
        )
        .trigger(availableNow=True)
        .toTable("bronze_stock_stream_final")
)

# COMMAND ----------

spark.table("bronze_stock_stream_final").count()

# COMMAND ----------

