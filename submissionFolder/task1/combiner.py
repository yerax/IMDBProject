#!/usr/bin/env python2
import sys

last_genre = None
min_val    = 0
last_val   = 0
sum_val    = 0
cnt_mvs    = 0


for line in sys.stdin:
    # Read each line that contains exactly one genre
    genre, mins = line.strip().split("|")

    if last_genre is None:
        last_genre = genre
        min_val = int(mins)
        sum_val = 0
        cnt_mvs = 0
    elif last_genre != genre:
        print(str(last_genre)+"|"+str(last_val)+"|"+str(sum_val)+"|"+str(min_val)+"|"+str(cnt_mvs))
        last_genre = genre
        min_val = int(mins)
        max_val = 0
        sum_val = 0
        cnt_mvs = 0

    last_val = mins
    cnt_mvs = cnt_mvs + 1
    sum_val = sum_val + int(mins)


# Don't forget the last genre of the input
print(str(last_genre)+"|"+str(last_val)+"|"+str(sum_val)+"|"+str(min_val)+"|"+str(cnt_mvs))
