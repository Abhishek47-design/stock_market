from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("StockMarketStreaming")
    .master("local[*]")
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1"
    )
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "stock-market")
    .option("startingOffsets", "latest")
    .load()
)

stock_df = df.selectExpr(
    "CAST(value AS STRING)"
)

query = (
    stock_df.writeStream
    .format("console")
    .outputMode("append")
    .option(
        "checkpointLocation",
        "data/checkpoints/stock_stream"
    )
    .start()
)

query.awaitTermination()