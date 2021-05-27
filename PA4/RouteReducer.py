#!/usr/bin/env python3

from operator import itemgetter
import sys  # for reading from stdin

current_route = None  # current route we are processing
current_route_delay = 0  # delay associated with this specific route run
route = None  # route we are about to get from stdin
current_count = 0  # how many times we have encountered this route

# input comes from stdin
for line in sys.stdin:
	line = line.strip()
	try:
		route, delay, count = line.split('\t')
		delay = float(delay)
		count = int(count)
	except ValueError:  # delay/count was NaN, ignore this line
		continue
	if current_route == route:
		current_route_delay += delay
		current_count += count
	else:
		if current_route:
			print(f"{current_route}\t{current_route_delay}\t{current_count}")
		current_route_delay = delay
		current_route = route
		current_count = count
if current_route == route:
	print(f"{current_route}\t{current_route_delay}\t{current_count}")
