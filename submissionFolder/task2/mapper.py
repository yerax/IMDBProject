#!/usr/bin/env python2
# Mapper in: title.basics.tsv out: [genre:str]
import sys

SKIPVAL = '\\N'
DELIM = '\t'

for line in sys.stdin:
    # Split each line of the table to obtain the fields of each column
    parts = line.strip().split(DELIM)

    # If the "genre" field in a line is empty, skip the line
    if len(parts) == 3:
        if float(parts[1]) >= 7.5 and int(parts[2]) >= 500000: # Good Rating
            print(parts[0]) # <tconst>
        else :
            continue
    elif len(parts) == 9:
        if parts[1] == SKIPVAL or parts[5] == SKIPVAL:
            continue
        elif parts[1] == "movie" and int(parts[5]) >= 1990 and int(parts[5]) <= 2018:
            print(str(parts[0])+"|"+str(parts[2])) # <tconst, title>
        else:
            continue
    else:
        continue
