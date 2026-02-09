cat > q6_mapper.py << 'PY'
#!/usr/bin/env python3
import sys
from log_parse import parse_line

for line in sys.stdin:
    p = parse_line(line)
    if not p:
        continue
    _, _, method, _, _, _ = p
    if method == "POST":
        print("post\t1")
PY
chmod +x q6_mapper.py

"""
hdfs dfs -rm -r -f /user/root/q6_out

hadoop jar "$STREAMING_JAR" \
  -D mapreduce.job.reduces=1 \
  -files /root/hadoop_mp1/q6_mapper.py,/root/hadoop_mp1/sum_reducer.py,/root/hadoop_mp1/log_parse.py \
  -mapper q6_mapper.py \
  -reducer sum_reducer.py \
  -input "$LOG_IN" \
  -output /user/root/q6_out

hdfs dfs -cat /user/root/q6_out/part-00000
