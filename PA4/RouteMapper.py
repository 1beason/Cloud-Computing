#!/usr/bin/env python3

import sys, csv  # import sys for reading stdin, csv for parsing lines

reader = csv.reader(sys.stdin, delimiter=',') # telling csv to read from stdin

worst_airlines = ['OH', 'G4', 'YV']  # the top 3 worst airlines in jan 2021

for row in reader:
	if row[1] in worst_airlines: # only want to process the worst airlines
		print(f"{row[4]}->{row[8]}:{row[1]}\t{row[12]}\t1")  # print orig_id, dest_id, delay, and frequency delimited by tabs
