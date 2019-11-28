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
        if parts[2] == SKIPVAL:
            continue
        elif isinstance(parts[2], int):
            print (parts[0]+"|"+parts[2]) # <tconst, numVotes>
        else:
            for writter in parts[2].split(','):
                print (parts[0]+"|"+writter) # <tconst, nconst>

    elif len(parts) == 6:
        if parts[1] == SKIPVAL or parts[5] == SKIPVAL:
            continue
        else:
            for tconst in parts[5].split(','):
                print (tconst +"|"+parts[0]+"|"+parts[1]) # <tconst, nconst, name>
