#!/usr/bin/env python3

f = open('example.txt')
#f = open('input.txt')

# Load grid
grid = []
for line in f:
   line = line.strip()
   row = [ c for c in line ]
   grid += [ row ]
H = len(grid)
W = len(grid[0])

# Load lines like: "123: 234 345 456 567 678"
for line in f:
	parts = re.split(':', line.strip())
	target = int(parts[0])
	values = [int(x) for x in parts[1].split()]
