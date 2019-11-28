#!/usr/bin/env python2
import sys

count = 10
# NEED TO CHECK REPEATED VALUES
for line in sys.stdin:
    if count > 0:
       parts = line.strip().split("|")
       print(parts[0]+"|"+parts[1])
       count = count - 1
