#!/usr/bin/env python3

def process(filename):
    # Load grid
    grid = []
    for line in open(filename):
        line = line.strip()
        row = [ c for c in line ]
        grid += [ row ]
    H = len(grid)
    W = len(grid[0])

    # Load lines like: "123: 234 345 456 567 678"
    for line in open(filename):
        parts = re.split(':', line.strip())
        target = int(parts[0])
        values = [int(x) for x in parts[1].split()]

    sum = 0
    print(filename, sum)
    return sum


assert(process("example.txt") == 0)
assert(process("input.txt") == 0)
