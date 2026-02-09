# INFSCI 2750 -- Mini Project 1 -- Donat Fabian

## Hadoop in Docker + MapReduce Log Analysis

Our project sets up a single-node Hadoop cluster using Docker and
implements Hadoop Streaming MapReduce programs to:

-   Compute character n-gram frequencies (Part 2)
-   Analyze a real access log file using MapReduce (Part 3, Questions
    5--10)

The Hadoop cluster runs in a Docker container and supports HDFS and
MapReduce execution in local single-node mode.

------------------------------------------------------------------------

# Part 1 - Hadoop in Docker

## 1. Building the Docker Image

From the directory containing the `Dockerfile`:

    docker build -t infsci2750-hadoop .

------------------------------------------------------------------------

## 2. Start the Container

    docker run -it --name hadoop2750 infsci2750-hadoop bash

If the container already exists:

    docker start hadoop2750
    docker exec -it hadoop2750 bash

------------------------------------------------------------------------

## 3. Environment Setup Inside Container

    export HADOOP_HOME=/opt/hadoop
    export PATH="$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH"
    export STREAMING_JAR=/opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar

------------------------------------------------------------------------

# Part 2 -- N-Gram Frequency Program

The program computes character n-grams for a given input text.

Example (n=2, input: "Helloworld"):

    He 1
    el 1
    ll 1
    lo 1
    ow 1
    wo 1
    or 1
    rl 1
    ld 1

------------------------------------------------------------------------

## Test File

    printf "Helloworld" > helloworld.txt
    hdfs dfs -put -f helloworld.txt /user/root/helloworld.txt

------------------------------------------------------------------------

## Run N-Gram Job

    hdfs dfs -rm -r -f /user/root/ngram_out

    hadoop jar "$STREAMING_JAR"       -D mapreduce.job.reduces=1       -files ngram_mapper.py,sum_reducer.py       -mapper ngram_mapper.py       -reducer sum_reducer.py       -input /user/root/helloworld.txt       -output /user/root/ngram_out       -cmdenv N=2

View results:

    hdfs dfs -cat /user/root/ngram_out/part-00000

------------------------------------------------------------------------
# Part 3 -- Log File Analysis (Q1--Q4)

-- place code here -- 

# Part 3 -- Log File Analysis (Q5--Q10)

## Log File Upload

    hdfs dfs -put -f /root/access_log /user/root/access_log

Input path used:

    /user/root/access_log

------------------------------------------------------------------------

# Q5

### Which IP accesses the website most? How many accesses?

Output location:

    /user/root/q5_out

------------------------------------------------------------------------

# Q6

### How many POST requests were made?

Output location:

    /user/root/q6_out

------------------------------------------------------------------------

# Q7

### How many requests received a 404 status code?

Output location:

    /user/root/q7_out

------------------------------------------------------------------------

# Q8

### How much data was requested on 19/Dec/2020?

Output location:

    /user/root/q8_out

------------------------------------------------------------------------

# Q9

### List 3 IPs that access the website most and total data size for each

Output location:

    /user/root/q9_out

------------------------------------------------------------------------

# Q10

### How much data (bytes) was successfully (status 200) requested on 16/Jan/2022?

Output location:

    /user/root/q10_out

------------------------------------------------------------------------

# Summary

This project in summary demonstrates:

-   Building a Hadoop single-node cluster in Docker
-   Managing HDFS input/output
-   Implementing MapReduce programs using Hadoop Streaming
-   Processing large log files
-   Extracting structured insights from web server logs
