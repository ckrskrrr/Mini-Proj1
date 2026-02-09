#!/usr/bin/env python3
import sys

current_key = None
current_sum = 0

def flush():
    global current_key, current_sum
    if current_key is not None:
        sys.stdout.write("{}\t{}\n".format(current_key, current_sum))

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        key, val = line.split("\t", 1)
        val = int(val)
    except ValueError:
        continue

    if current_key is None:
        current_key = key
        current_sum = val
    elif key == current_key:
        current_sum += val
    else:
        flush()
        current_key = key
        current_sum = val

flush()
