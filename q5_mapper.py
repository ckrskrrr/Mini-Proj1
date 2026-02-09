cat > q5_mapper.py << 'PY'
#!/usr/bin/env python3
import sys
from log_parse import parse_line

for line in sys.stdin:
    p = parse_line(line)
    if not p:
        continue
    ip, _, _, _, _, _ = p
    print(f"{ip}\t1")
PY
chmod +x q5_mapper.py

"""
to run

hdfs dfs -rm -r -f /user/root/q5_out

hadoop jar "$STREAMING_JAR" \
  -D mapreduce.job.reduces=1 \
  -files /root/hadoop_mp1/q5_mapper.py,/root/hadoop_mp1/top1_reducer.py,/root/hadoop_mp1/log_parse.py \
  -mapper q5_mapper.py \
  -reducer top1_reducer.py \
  -input "$LOG_IN" \
  -output /user/root/q5_out

hdfs dfs -cat /user/root/q5_out/part-00000
