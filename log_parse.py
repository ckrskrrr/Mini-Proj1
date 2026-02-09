## Shared parser

cat > log_parse.py << 'PY'
import re

LOG_RE = re.compile(
    r'^(?P<ip>\S+)\s+\S+\s+\S+\s+\[(?P<time>[^\]]+)\]\s+"(?P<method>\S+)\s+(?P<path>\S+)\s+\S+"\s+(?P<status>\d{3})\s+(?P<size>\S+)'
)

def parse_line(line: str):
    m = LOG_RE.match(line)
    if not m:
        return None
    ip = m.group("ip")
    t = m.group("time")  # e.g. 15/Jul/2009:15:50:35 -0700
    method = m.group("method")
    raw_path = m.group("path")
    path = raw_path.split("?", 1)[0]
    status = m.group("status")
    size_raw = m.group("size")
    size = 0 if size_raw == "-" else int(size_raw)
    return ip, t, method, path, status, size
PY