#!/usr/bin/env python2
import sys
# Needs to be executed in one single reducer as we want the result to be sorted
last_dec = None
last_gen = None

for line in sys.stdin:
    input_line = line.strip().split("|") # <dec, gen, rate, title>
    if last_dec is None and last_gen is None:
        # Initial Case
        last_dec = input_line[0]
        last_gen = input_line[1]
        print (input_line[0]+"|"+input_line[1]+"|"+input_line[3])
    elif last_dec == input_line[0] and last_gen != input_line[1]:
        # Case Change of Last gen
        last_gen = input_line[1]
        print (input_line[0]+"|"+input_line[1]+"|"+input_line[3])
    elif last_dec != input_line[0]:
        last_dec = input_line[0]
        last_gen = input_line[1]
        print (input_line[0]+"|"+input_line[1]+"|"+input_line[3])
