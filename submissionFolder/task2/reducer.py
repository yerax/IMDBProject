#!/usr/bin/env python2
# I have not used a combiner because the combiner need the input to be sorted in order to optimize the code, otherwise it is just extra work that is rarely efficient.
import sys

last_const = None
aux_title  = None

for line in sys.stdin:
    # Read each line that contains exactly one genre
    input_line = line.strip().split("|")
    if last_const is None:
        last_const = input_line[0]
        if len(input_line) == 2:
            aux_title = input_line[1]
        elif len(input_line) == 1:
            aux_title = None

    elif last_const != input_line[0]:
        last_const = input_line[0]
        if len(input_line) == 2:
            aux_title = input_line[1]
        elif len(input_line) == 1:
            aux_title = None
    else:
        #Means Valid in both files
        if aux_title is not None:
            print(aux_title)
        else:
            print(input_line[1])

        # Allow no duplicates in the output




# Don't forget the last genre of the input
