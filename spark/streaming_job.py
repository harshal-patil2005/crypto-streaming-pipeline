
import json
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, DoubleType
from pyspark.sql.functions import col, lit, avg, window, when, to_timestamp

# -------------------------
# READ INR RATE
# -------------------------
with open("/content/crypto-streaming-pipeline/data/inr_rate.json", "r") as f:
    rate = json.load(f)["inr_rate"]

print("Using INR rate:", rate)

# -------------------------
# SPARK SESSION
# -------------------------
spark = SparkSession.builder \
    .appName("CryptoStreaming") \
    .getOrCreate()

# -------------------------
# SCHEMA
# -------------------------
schema = StructType() \
    .add("timestamp", StringType()) \
    .add("asset", StringType()) \
    .add("price", DoubleType())

# -------------------------
# STREAM READ
# -------------------------
df = spark.readStream \
    .option("header", True) \
    .option("maxFilesPerTrigger", 1) \
    .schema(schema) \
    .csv("/content/crypto-streaming-pipeline/data/input_data")

# -------------------------
# PROCESSING
# -------------------------
df = df.withColumn(
    "timestamp",
    to_timestamp(col("timestamp"), "yyyy-MM-dd HH:mm:ss.SSSSSS")
).withWatermark("timestamp", "2 minutes")

processed_df = df \
    .filter(col("price") > 1000) \
    .withColumn("price_inr", col("price") * lit(rate))

# -------------------------
# WINDOWED AGGREGATION (STREAMING SAFE)
# -------------------------
agg_df = processed_df \
    .groupBy(
        window(col("timestamp"), "1 minute"),
        col("asset")
    ) \
    .agg(
        avg("price_inr").alias("avg_price_inr")
    )

# -------------------------
# ANOMALY FLAG
# -------------------------
final_df = agg_df.withColumn(
    "anomaly_flag",
    when(col("avg_price_inr") > 200000, "SPIKE").otherwise("NORMAL")
)

# -------------------------
# STREAM WRITE
# -------------------------
query = final_df.writeStream \
    .format("parquet") \
    .option("path", "/content/crypto-streaming-pipeline/data/output_data") \
    .option("checkpointLocation", "/content/crypto-streaming-pipeline/data/checkpoint") \
    .outputMode("append") \
    .start()
query.awaitTermination(60)
