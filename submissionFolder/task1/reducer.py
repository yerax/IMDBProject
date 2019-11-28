#!/usr/bin/env python2
# Reducer in: [genre:str]  out: [genre:str]
import sys

last_val = None
min_val  = 0
max_val  = 0
avg_sum  = 0
cnt_mvs  = 0
avg_val  = 0

# LINEAR BY ALL EXCEPT line 16 -> Should we consider it separated or what

for line in sys.stdin:
    # Read each line that contains exactly one genre
    parts = line.strip().split("|")
    # Case Not enter in the combiner
    if len(parts) == 2:
        if last_val is None:
            last_val = parts[0]
            min_val = int(parts[1])
            max_val = 0
            avg_sum = 0
            cnt_mvs = 0
        elif last_val != parts[0]:
            if cnt_mvs > 0:
                avg_val = float(float(avg_sum)/int(cnt_mvs))
            else :
                avg_val = 0

            print(str("{0:.2f}".format(round(avg_val,2)))+"|"+str(max_val)+"|"+str(min_val)+"|"+str(last_val))
            last_val = parts[0]
            min_val = int(parts[1])
            max_val = int(parts[1])
            avg_sum = 0
            cnt_mvs = 0

        cnt_mvs = cnt_mvs + 1
        avg_sum = avg_sum + int(parts[1])
        max_val = max(max_val, int(parts[1]))
    else:
        # The input is sorted but contains duplicates
        genre = parts[0]
        max_a = parts[1]
        sum_a = parts[2]
        min_a = parts[3]
        n     = parts[4]

        if last_val is None: # Don't forget the first genre of the input
            last_val = genre
            min_val  = int(min_a)
            max_val  = 0
            avg_sum  = 0
            cnt_mvs  = 0
        elif last_val != genre:
            # Allow no duplicates in the output
            # CALCULATE AVG NOW!
            if cnt_mvs > 0:
                avg_val = float(float(avg_sum)/int(cnt_mvs))
            else :
                avg_val = 0

            print(str("{0:.2f}".format(round(avg_val,2)))+"|"+str(max_val)+"|"+str(min_val)+"|"+str(last_val))
            last_val = genre
            min_val  = int(min_a)
            max_val  = 0
            avg_sum  = 0
            cnt_mvs  = 0


        cnt_mvs = cnt_mvs + int(n)
        avg_sum = avg_sum + int(sum_a)
        if min_a is not None:
            min_val = min(min_val,int(min_a))
        if max_a is not None:
            max_val = max(max_val,int(max_a))



# Don't forget the last genre of the input
if cnt_mvs:
    avg_val = float(float(avg_sum)/int(cnt_mvs))
else :
    avg_val = 0
print(str("{0:.2f}".format(round(avg_val,2)))+"|"+str(max_val)+"|"+str(min_val)+"|"+str(last_val))
