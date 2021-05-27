#!/usr/bin/env python3

import csv, sys  # import csv for reading file, sys for reading from stdin

reader = csv.reader(sys.stdin, delimiter=',')  # set up a csv reader for stdin

cancel_codes = ['A', 'B', 'C', 'D']  # the cancel codes we need to look for

for row in reader:
	if row[14] in cancel_codes:
		print(f'{row[14]}\t1')  # print the cancel code followed by its freq.

