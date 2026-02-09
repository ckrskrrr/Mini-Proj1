#!/usr/bin/env python3
import sys

PREFIX = "/images/smilies/"
TARGET_IP = "96.32.128.5"

def emit(k, v):
    sys.stdout.write("{}\t{}\n".format(k, v))

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split()
    if parts:
        ip = parts[0]

        # Q2
        if ip == TARGET_IP:
            emit("Q2_hits_from_ip", 1)

        # Q5
        emit("Q5_ip::{}".format(ip), 1)
    else:
        continue

    q1_done = False
    q3_done = False
    q4_done = False

    first_quote = line.find('"')
    if first_quote != -1:
        second_quote = line.find('"', first_quote + 1)
        if second_quote != -1:
            request = line[first_quote + 1: second_quote]
            req_parts = request.split()
            if len(req_parts) >= 2:
                method = req_parts[0]
                url = req_parts[1]

                # Q3
                emit("Q3_method::{}".format(method), 1)

                # Path for Q1/Q4
                path = url.split("?", 1)[0]

                # Q1
                if path.startswith(PREFIX):
                    emit("Q1_smilies_hits", 1)

                # Q4
                emit("Q4_path::{}".format(path), 1)
