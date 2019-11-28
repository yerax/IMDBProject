#!/usr/bin/env python2
# Mapper in: title.basics.tsv out: [genre:str]
import sys

SKIPVAL = '\\N'
DELIM = '\t'

for line in sys.stdin:
    # Split each line of the table to obtain the fields of each column
    parts = line.strip().split("|")
    if parts[0] == SKIPVAL or parts[1] == SKIPVAL:
        continue
    else:
        print(parts[0]+"|"+parts[1])
