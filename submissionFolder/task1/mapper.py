#!/usr/bin/env python2
import sys

SKIPVAL = '\\N'
DELIM = '\t'

for line in sys.stdin:
    # Split each line of the table to obtain the fields of each column
    parts = line.strip().split(DELIM)

    # If the "genre" field in a line is empty, skip the line
    if parts[-1] == SKIPVAL:
        continue

    # Each title can have multiple genres, need to split
    for genre in parts[-1].split(','):
        # Yield all genres of the title, one per output line
        if parts[7] != SKIPVAL:
            print(genre +"|"+ parts[7])
            # Sends to pipe <genre,title>
