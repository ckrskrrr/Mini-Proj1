cat > q9_mapper.py << 'PY'
#!/usr/bin/env python3
import sys
from log_parse import parse_line

for line in sys.stdin:
    p = parse_line(line)
    if not p:
        continue
    ip, _, _, _, _, size = p
    print(f"{ip}\t1\t{size}")
PY
chmod +x q9_mapper.py

""""

hdfs dfs -rm -r -f /user/root/q9_out

hadoop jar "$STREAMING_JAR" \
  -D mapreduce.job.reduces=1 \
  -files /root/hadoop_mp1/q9_mapper.py,/root/hadoop_mp1/top3_ip_reducer.py,/root/hadoop_mp1/log_parse.py \
  -mapper q9_mapper.py \
  -reducer top3_ip_reducer.py \
  -input "$LOG_IN" \
  -output /user/root/q9_out

hdfs dfs -cat /user/root/q9_out/part-00000
