
import pyspark

my_spark = pyspark.sql.SparkSession \
    .builder \
    .appName("myApp") \
    .config("spark.jars.packages","*")\
    .config('spark.jars.packages','org.mongodb.spark:mongo-spark-connector_2.11:2.3.1' )\
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/database.factures") \
    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/database.factures") \
    .getOrCreate()\

df = my_spark.read.format("com.mongodb.spark.sql.DefaultSource").load()
df.printSchema()

#./bin/spark-submit   --master spark://192.168.56.101:7077   examples/src/main/python/wordcount.py   /usr/local/spark/LICENSE 
