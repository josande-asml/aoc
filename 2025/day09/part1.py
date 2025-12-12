#!/usr/bin/env python3

def process(filename):
    # Load tile coordinates
    tiles = []
    for line in open(filename):
        (x, y) = line.strip().split(',')
        tiles += [ (int(x), int(y)) ]

    # Try all combinations
    max_area = 0
    for i in range(len(tiles)-1):
        (xi,yi) = tiles[i]
        for j in range(len(tiles)):
            (xj,yj) = tiles[j]
            area = (abs(xi-xj)+1)*(abs(yi-yj)+1)
            max_area = max(max_area, area)

    print(filename, max_area)
    return max_area


assert(process("example.txt") == 50)
assert(process("input.txt") == 4749929916)
