cat > sum_reducer.py << 'PY'
#!/usr/bin/env python3
import sys

current = None
total = 0

for line in sys.stdin:
    key, val = line.rstrip("\n").split("\t", 1)
    val = int(val)

    if current is None:
        current = key

    if key != current:
        print(f"{current}\t{total}")
        current = key
        total = 0

    total += val

if current is not None:
    print(f"{current}\t{total}")
PY
chmod +x sum_reducer.py