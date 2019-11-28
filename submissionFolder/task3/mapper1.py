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
        print(parts[0]+"|"+parts[1]) # <tconst, rate>
    elif len(parts) == 9:
        if parts[1] == SKIPVAL or parts[5] == SKIPVAL or parts[8] == SKIPVAL:
            continue
        elif parts[1] == "movie" and int(parts[5]) >= 1900 and int(parts[5]) <= 1999:
            for genre in parts[8].split(','):
                print(parts[0]+"|"+parts[2]+"|"+parts[5][2]+"|"+genre) # <tconst, title, decade, genre>
    else:
        continue
