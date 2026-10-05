from pyspark import pipelines as dp
from pyspark.sql import functions as F


@dp.materialized_view
def bronze_customers():
    return (
        spark.read
        .option("header", "true")
        .option("inferSchema", "true")
        .csv("../data/customers/dim_customers.csv")
    )


# @dp.materialized_view
# def silver_customers():
#     return (
#         spark.read.table("bronze_customers")
#         .filter(F.col("customer_id").isNotNull())
#         .filter(F.col("amount") > 0)
#     )


# @dp.materialized_view
# def customer_summary():
#     return (
#         spark.read.table("silver_customers")
#         .groupBy("country")
#         .agg(
#             F.count("*").alias("customer_count"),
#             F.sum("amount").alias("total_amount")
#         )
#     )