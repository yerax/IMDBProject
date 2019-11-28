#!/usr/bin/env python2
import sys

last_vote = None
last_title = None
last_writter = None


for line in sys.stdin:
    # Read each line that contains exactly one genre
    parts = line.strip().split("|")
    if len(parts) == 4:
        print (parts[0]+"|"+parts[1])
    else:
        if last_title is None and parts[1][0] != "n":
            last_title = parts[0]
            last_vote  = parts[1]
        elif last_title != parts[0] and parts[1][0] != "n":
            last_title = parts[0]
            last_vote  = parts[1]
        elif last_title == parts[0] and len(parts) == 2:
            last_writter = parts[1]
        elif last_title == parts[0] and len(parts) == 3 and last_writter == parts[1]: # case join of three properties
            print(last_vote+"|"+parts[2])
