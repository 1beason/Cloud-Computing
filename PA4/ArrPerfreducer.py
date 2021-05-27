#!/usr/bin/env python3

from operator import itemgetter
import sys

current_airline = None
current_arr_delay = 0
airline = None
current_count = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
        line = line.strip()

        # parse the input we got from mapper.py
        try:
            airline, arr_delay, count = line.split('\t')
            arr_delay = float(arr_delay)
            count = int(count)
        except ValueError:
            # count was not a number, so silently
            # ignore/discard this line
            continue

        # this IF-switch only works because Hadoop sorts map output
        # by key (here: word) before it is passed to the reducer
        if current_airline == airline:
            current_arr_delay += arr_delay
            current_count += count
        else:
            if current_airline:
                    # write result to STDOUT
                    print("{0}\t{1}\t{2}".format(current_airline, current_arr_delay, current_count))
            current_arr_delay = arr_delay
            current_airline = airline
            current_count = count

# do not forget to output the last word if needed!
if current_airline == airline:
    print("{0}\t{1}\t{2}".format(current_airline, current_arr_delay, current_count))
