chmod +x mapper_q1_q5.py reducer_q1_q5.py

# make sure log is in HDFS
hdfs dfs -mkdir -p /logs
hdfs dfs -put -f /project/part3/access_log /logs/access_log

hdfs dfs -rm -r -f /out_q1_q5

hadoop jar "$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-"*.jar \
  -files /project/part3/mapper_q1_q5.py,/project/part3/reducer_q1_q5.py \
  -mapper mapper_q1_q5.py \
  -reducer reducer_q1_q5.py \
  -input /logs/access_log \
  -output /out_q1_q5

hdfs dfs -cat /out_q1_q5/part-* > /tmp/q1_q5_out.txt
#Q1: How many hits were made to the website directory 
grep '^Q1_smilies_hits' /tmp/q1_q5_out.txt

#Q2: How many hits were made from the IP: 96.32.128.5?
grep '^Q2_hits_from_ip' /tmp/q1_q5_out.txt

#Q3: How many HTTP request methods are used in this file? What are they?
grep '^Q3_method::' /tmp/q1_q5_out.txt
grep '^Q3_method::' /tmp/q1_q5_out.txt | wc -l

#Q4: Which path in the website has been hit most? How many hits were made to the path? 
grep '^Q4_path::' /tmp/q1_q5_out.txt | sort -k2,2nr | head -n 1

#Q5: Which IP accesses the website most? How many accesses were made by it? 
grep '^Q5_ip::' /tmp/q1_q5_out.txt | sort -k2,2nr | head -n 1





