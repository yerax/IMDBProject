#!/usr/bin/env python2
# Mapper in: title.basics.tsv out: [genre:str]
import sys


for line in sys.stdin:
    # Split each line of the table to obtain the fields of each column
    parts = line.strip().split("|")
    print (parts[0]+"|"+parts[1]+"|"+parts[2]+"|"+parts[3])
