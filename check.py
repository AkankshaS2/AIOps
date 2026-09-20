# import pyspark
# print(pyspark.__version__)
from pyspark.sql import SparkSession
spark=SparkSession.builder\
.appName("SparkApp")\
.getOrCreate()

data=[
    ("server1",56),
    ("server1",56),
    ("server1",56),
    ("server1",56),
    ("server1",56),
    ("server1",56)

]df.sp