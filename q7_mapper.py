cat > q7_mapper.py << 'PY'
#!/usr/bin/env python3
import sys
from log_parse import parse_line

for line in sys.stdin:
    p = parse_line(line)
    if not p:
        continue
    _, _, _, _, status, _ = p
    if status == "404":
        print("404\t1")
PY
chmod +x q7_mapper.py

""""

hdfs dfs -rm -r -f /user/root/q7_out

hadoop jar "$STREAMING_JAR" \
  -D mapreduce.job.reduces=1 \
  -files /root/hadoop_mp1/q7_mapper.py,/root/hadoop_mp1/sum_reducer.py,/root/hadoop_mp1/log_parse.py \
  -mapper q7_mapper.py \
  -reducer sum_reducer.py \
  -input "$LOG_IN" \
  -output /user/root/q7_out

hdfs dfs -cat /user/root/q7_out/part-00000
