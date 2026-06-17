from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("StockMarketProject")
    .master("local[*]")
    .getOrCreate()
)

print("Spark Session Created Successfully")

spark.stop()