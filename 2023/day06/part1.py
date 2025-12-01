#!/usr/bin/env python3

def process(filename):
	f = open(filename)
	times = f.readline().split()
	distances = f.readline().split()
	races = []
	for i in range(1, len(times)):
		races += [ (int(times[i]), int(distances[i])) ]
	print(races)

	total = 1
	for race in races:
		count = 0
		for t in range(1, race[0]):
			distance = (race[0]-t)*t
			if distance > race[1]:
				count += 1
		total *= count
			
	print(filename, total)
	return total


assert(process("example.txt") == 288)
assert(process("input.txt") == 4403592)
