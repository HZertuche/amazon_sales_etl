import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

from pyspark.sql.functions import (
    regexp_replace,
    col,
    split,
    trim,
    size,
    max as spark_max
)

from pyspark.sql.types import DecimalType, StringType

# Working with glue
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read input file
df = spark.read.csv(
    "s3://amazon-sales-github/prueba/amazon.csv",
    header=True,
    multiLine=True,
    quote='"',
    escape='"'
)

# Delete the characters at the beginning of the text and only show the numbers, change it to decimal format
df = df.withColumn(
    "discounted_price",
    regexp_replace(col("discounted_price"), "[^0-9.]", "").cast(DecimalType(10,2))
)

df = df.withColumn(
    "actual_price",
    regexp_replace(col("actual_price"), "[^0-9.]", "").cast(DecimalType(10,2))
)

# Change the columns to string format
string_cols = [
    "product_id",
    "product_name",
    "category",
    "discount_percentage",
    "rating_count"
]

for c in string_cols:
    df = df.withColumn(c, col(c).cast(StringType()))

# Change rating to decimal format
df = df.withColumn(
    "rating",
    col("rating").cast(DecimalType(3,2))
)

# Divide the text from the column "category" to create subcategories
df = df.withColumn(
    "category_array",
    split(col("category"), "\\|")
)

max_levels = df.select(
    spark_max(size(col("category_array"))).alias("max_levels")
).collect()[0]["max_levels"]

for i in range(max_levels):
    df = df.withColumn(
        f"category_lvl{i+1}",
        trim(col("category_array").getItem(i))
    )

# Select the columns to show
cols_to_keep = [
    "product_id",
    "product_name",
    "discounted_price",
    "actual_price",
    "discount_percentage",
    "rating",
    "rating_count"
] + [f"category_lvl{i+1}" for i in range(max_levels)]

df_final = df.select(cols_to_keep)

# Change to a DynamicFrame
dyf = DynamicFrame.fromDF(df_final, glueContext, "dyf")


# Save it in S3 with a Parquet format with Snappy compression
df_final.coalesce(1).write.mode("overwrite").parquet(
    "s3://amazon-sales-github/outputv2/",
    compression="snappy"
)

job.commit()