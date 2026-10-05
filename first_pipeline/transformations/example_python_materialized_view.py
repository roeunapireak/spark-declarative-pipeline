from pyspark import pipelines as dp
from pyspark.sql import DataFrame

@dp.materialized_view
def example_python_materialized_view() -> DataFrame:
    return spark.range(10)
