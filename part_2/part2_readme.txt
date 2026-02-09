SETUP STEPS:
------------

1. Start Docker container (in one terminal - leave it running):
   docker run -it -p 9870:9870 -p 8088:8088 --name hadoop-container proj1

2. Open a second terminal and copy source code to container:
   docker cp NGram.java hadoop-container:/root/

3. In a third terminal, enter the container:
   docker exec -it hadoop-container bash
   cd /root


COMPILE:
--------

mkdir ngram_classes
javac -classpath $(hadoop classpath) -d ngram_classes NGram.java
jar -cvf ngram.jar -C ngram_classes/ .


TEST 1: HELLOWORLD
------------------

echo "Helloworld" > input.txt
hdfs dfs -mkdir -p /user/root/ngram_input
hdfs dfs -put input.txt /user/root/ngram_input/
hadoop jar ngram.jar NGram 2 /user/root/ngram_input /user/root/ngram_output
hdfs dfs -cat /user/root/ngram_output/part-r-00000


TEST 2: LARGE DATASET
---------------------

# if you already have an output file from previous runs-
hdfs dfs -rm -r /user/root/ngram_output   # <- do this first

# otherwise: 
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar randomtextwriter -Dmapreduce.randomtextwriter.totalbytes=5000000 /user/root/random_text
hadoop jar ngram.jar NGram 3 /user/root/random_text /user/root/ngram_output
hdfs dfs -cat /user/root/ngram_output/part-r-00000 | head -30


USAGE:
------

hadoop jar ngram.jar NGram <n> <input_path> <output_path>

n = size of n-grams (2 for bigrams, 3 for trigrams)
input_path = HDFS input directory
output_path = HDFS output directory (must not exist)