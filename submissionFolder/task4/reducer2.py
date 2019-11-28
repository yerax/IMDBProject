#!/usr/bin/env python2
import sys

count = 10
top10 = []
# In order to check for repeated values we have a vector of names
for line in sys.stdin:
    if count > 0:
        parts = line.strip().split("|")
        if parts[1] not in top10:
           top10.append(parts[1])
           print(parts[0]+"|"+parts[1])
           count = count - 1
