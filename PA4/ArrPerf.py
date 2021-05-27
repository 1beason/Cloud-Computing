#!/usr/bin/env python3

import sys, csv
reader = csv.reader(sys.stdin, delimiter=',') # piping stdin to csv reader to parse lines easily
for row in reader:  # now read each row
	print(f'{row[1]}\t{row[12]}\t1')  # print the Airline code and the arrival delay, and the frequency of this flight (trivially 1) delimited by tabs

