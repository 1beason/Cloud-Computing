#!/usr/bin/env python3

from operator import itemgetter
import sys  # import sys to read stdin

current_code = None  # current cancellation code
current_count = 0  # currnt count of current code

# mapping the data we get from mapper to more readable output
cancel_dict = {'A': 'Carrier', 'B':'Weather', 'C':'National Air System', 'D':'Security'}


for line in sys.stdin:
	line = line.strip()
	try:
		code, count = line.split('\t')
		count = int(count)
	except ValueError:
		continue  # problem reading the stdin so forget this line and move on

	if current_code == code:
		current_count += count
	else:
		if current_code:
			print(f'{cancel_dict[current_code]}\t{current_count}')
		current_code = code
		current_count = count
if current_code == code:
	print(f'{cancel_dict[current_code]}\t{current_count}')
