cat > q8_mapper.py << 'PY'
#!/usr/bin/env python3
import sys
from log_parse import parse_line

DATE_PREFIX = "19/Dec/2020:"

for line in sys.stdin:
    p = parse_line(line)
    if not p:
        continue
    _, t, _, _, _, size = p
    if t.startswith(DATE_PREFIX):
        print(f"bytes\t{size}")
PY
chmod +x q8_mapper.py

""""

hdfs dfs -rm -r -f /user/root/q8_out

hadoop jar "$STREAMING_JAR" \
  -D mapreduce.job.reduces=1 \
  -files /root/hadoop_mp1/q8_mapper.py,/root/hadoop_mp1/sum_reducer.py,/root/hadoop_mp1/log_parse.py \
  -mapper q8_mapper.py \
  -reducer sum_reducer.py \
  -input "$LOG_IN" \
  -output /user/root/q8_out

hdfs dfs -cat /user/root/q8_out/part-00000
