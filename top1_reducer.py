cat > top1_reducer.py << 'PY'
#!/usr/bin/env python3
import sys

current = None
total = 0
best_key = None
best_val = -1

def flush(k, v):
    global best_key, best_val
    if k is None:
        return
    if v > best_val:
        best_key, best_val = k, v

for line in sys.stdin:
    key, val = line.rstrip("\n").split("\t", 1)
    val = int(val)

    if current is None:
        current = key

    if key != current:
        flush(current, total)
        current = key
        total = 0

    total += val

flush(current, total)

if best_key is not None:
    print(f"{best_key}\t{best_val}")
PY
chmod +x top1_reducer.py