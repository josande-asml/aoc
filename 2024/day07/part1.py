#!/usr/bin/env python3
import re

#f = open('example.txt')
f = open('input.txt')
sum = 0
for line in f:
	parts = re.split(':', line.strip())
	target = int(parts[0])
	values = [int(x) for x in parts[1].split()]

	nrCombinations = 1 << len(values)
	for i in range(nrCombinations):
		out = values[0]
		for j in range(len(values)-1):
			if (i & (1 << j)) == 0:
				out += values[j+1]
			else:
				out *= values[j+1]
		if target == out:
			sum += target
			break
			
print(sum)  # 267566105056

