#!/usr/bin/env python3
import re

def process(filename):
    # Load grid
    grid = []
    for line in open(filename):
        row = re.split(' +', line.strip())
        grid += [ row ]
    H = len(grid)
    W = len(grid[0])

    sum = 0
    for x in range(W):
        if grid[H-1][x] == '+':
            answer = 0
            for y in range(H-1):
                answer += int(grid[y][x])
        else:
            answer = int(grid[0][x])
            for y in range(1,H-1):
                answer *= int(grid[y][x])
        sum += answer

    print(filename, sum)
    return sum


assert(process("example.txt") == 4277556)
assert(process("input.txt") == 4076006202939)
