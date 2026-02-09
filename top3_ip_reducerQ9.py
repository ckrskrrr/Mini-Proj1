cat > top3_ip_reducer.py << 'PY'
#!/usr/bin/env python3
import sys

current = None
count = 0
bytes_sum = 0
top = []  # (count, ip, bytes)

def push(ip, c, b):
    if ip is not None:
        top.append((c, ip, b))

for line in sys.stdin:
    parts = line.rstrip("\n").split("\t")
    if len(parts) != 3:
        continue
    ip, c, b = parts
    c = int(c); b = int(b)

    if current is None:
        current = ip

    if ip != current:
        push(current, count, bytes_sum)
        current = ip
        count = 0
        bytes_sum = 0

    count += c
    bytes_sum += b

push(current, count, bytes_sum)

top.sort(reverse=True, key=lambda x: x[0])

for c, ip, b in top[:3]:
    print(f"{ip}\t{c}\t{b}")
PY
chmod +x top3_ip_reducer.py