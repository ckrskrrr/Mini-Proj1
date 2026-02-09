cat > q10_mapper.py << 'PY'
#!/usr/bin/env python3
import sys
from log_parse import parse_line

DATE_PREFIX = "16/Jan/2022:"

for line in sys.stdin:
    p = parse_line(line)
    if not p:
        continue
    _, t, _, _, status, size = p
    if status == "200" and t.startswith(DATE_PREFIX):
        print(f"bytes\t{size}")
PY
chmod +x q10_mapper.py

""""

hdfs dfs -rm -r -f /user/root/q10_out

hadoop jar "$STREAMING_JAR" \
  -D mapreduce.job.reduces=1 \
  -files /root/hadoop_mp1/q10_mapper.py,/root/hadoop_mp1/sum_reducer.py,/root/hadoop_mp1/log_parse.py \
  -mapper q10_mapper.py \
  -reducer sum_reducer.py \
  -input "$LOG_IN" \
  -output /user/root/q10_out

hdfs dfs -cat /user/root/q10_out/part-00000
