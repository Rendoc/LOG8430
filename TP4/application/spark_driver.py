
import pyspark
from pyspark.sql import functions 
from pyspark.mllib.fpm import FPGrowth
import json
import re
import unicodedata

my_spark = pyspark.sql.SparkSession \
    .builder \
    .appName("RESTAPI_most_frequent") \
    .master("192.168.56.101:7077") \
    .config('spark.jars.packages','org.mongodb.spark:mongo-spark-connector_2.11:2.3.1' ) \
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/conception.factures") \
    .getOrCreate()



#.config("spark.mongodb.output.uri", "mongodb://127.0.0.1/conception.factures") \
df = my_spark.read.format("com.mongodb.spark.sql.DefaultSource").load()

#./bin/spark-submit   --master spark://192.168.56.101:7077   examples/src/main/python/wordcount.py   /usr/local/spark/LICENSE 
#./bin/spark-submit   --master spark://192.168.56.101:7077   examples/src/main/python/pi.py   12


def get_most():
    transactions = df.groupBy("_id") \
                .agg(functions.collect_list("items.name").alias("product_name")) \
                .rdd \
                .flatMap(lambda x: x.product_name)
    
    transactions.collect()

    model = FPGrowth.train(transactions, minSupport=0.2, numPartitions=10)
    result = model.freqItemsets().collect()
    print(result)
    """ stripped_result = []

    for fi in result:
        result_line = unicode(fi)
        words, freq = re.search(r'FreqItemset\(items=\[(.*)\], freq=(\d*)\)', "%s" %result_line).groups()
        stripped_result.append({'product': words, 'freq': int(freq)})
    
    return json.dumps(stripped_result, indent=4, sort_keys=True) """
