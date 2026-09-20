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

]df.sp wget https://downloads.apache.org/kafka/4.1.0/kafka_2.13-4.1.0.tgz 