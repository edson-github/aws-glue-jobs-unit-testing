from pyspark import SparkContext
from awsglue.context import GlueContext
import pytest


@pytest.fixture(scope="session")
def glueContext():
    """
    Function to setup test environment for PySpark and Glue
    """
    spark_context = SparkContext()
    yield GlueContext(spark_context)
    spark_context.stop()
