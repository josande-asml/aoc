#!/usr/bin/env python3

import math

def process(filename):
	f = open(filename)
	times = f.readline().split()
	distances = f.readline().split()
	time = int("".join(times[1:]))
	record = int("".join(distances[1:]))

	# distance = (time - t)*t
	# distance > record
	#
	# solve: t^2 - time*t + record = 0
	D = math.sqrt(time*time - 4*record)
	min_t = (time - D)/2
	max_t = (time + D)/2
	nrWins = int(round(math.floor(max_t) - math.ceil(min_t))) + 1
	
	print(filename, nrWins)
	return nrWins
	

assert(process("example.txt") == 71503)
assert(process("input.txt") == 38017587)
