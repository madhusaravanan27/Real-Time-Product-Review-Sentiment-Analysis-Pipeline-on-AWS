from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, when

spark = SparkSession.builder.appName("SentimentAnalysis").getOrCreate()

# Load raw reviews from S3
df = spark.read.json("s3://productreview-pipeline/raw-reviews/")

# Add sentiment classification
df = df.withColumn("review_lower", lower(col("review")))
df = df.withColumn("sentiment", when(
    col("review_lower").rlike("amazing|love|great|fantastic|happy|excellent"), "Positive"
).when(
    col("review_lower").rlike("terrible|bad|worst|broke|horrible|poor"), "Negative"
).otherwise("Neutral"))

df = df.drop("review_lower")

# Save processed reviews to S3
df.write.mode("overwrite").json("s3://productreview-pipeline/processed-reviews/")
