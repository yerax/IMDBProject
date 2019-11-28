#!/usr/bin/env python2
import sys

last_const = None
aux_rate   = None

for line in sys.stdin:
    # Read each line that contains exactly one genre
    input_line = line.strip().split("|")
    if last_const is None:
        last_const = input_line[0]
        if len(input_line) == 2:
            aux_rate = input_line[1]

    elif last_const != input_line[0]:
        last_const = input_line[0]
        if len(input_line) == 2:
            aux_rate = input_line[1]
        else:
            last_const = None
            aux_rate   = None

    else:
        if aux_rate is not None:
            print(input_line[2]+"|"+input_line[3]+"|"+aux_rate+"|"+input_line[1])
        else:
            continue
