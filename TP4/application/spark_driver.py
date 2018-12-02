
import pyspark
from pyspark.sql import functions 
from pyspark.mllib.fpm import FPGrowth
import json
import re
import unicodedata

def get_most():
    print("get most")
    my_spark = pyspark.sql.SparkSession \
        .builder \
        .appName("RESTAPI_most_frequent") \
        .master("local[2]") \
        .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/conception.factures") \
        .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/conception.factures") \
        .config('spark.jars.packages','org.mongodb.spark:mongo-spark-connector_2.11:2.3.1' )\
        .config("spark.executor.memory","1G") \
        .config("spark.driver.memory","5G") \
        .getOrCreate()\

    df = my_spark.read.format("com.mongodb.spark.sql.DefaultSource").load()
    
    df.show()

    transactions = df.groupBy("_id") \
                .agg(functions.collect_list("articles.product_name").alias("name")) \
                .rdd \
                .flatMap(lambda x: x.name)
    
    transactions.collect()

    model = FPGrowth.train(transactions, minSupport=0.2, numPartitions=10)
    result = model.freqItemsets().collect()
    
    return json.dumps(result)

