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

    # Find starting point
    for x in range(W):
        if grid[0][x] == 'S':
            beams = [ x ]
            break

    # Simulate beam splitting
    sum = 0
    for y in range(2, H-1, 2):
        new_beams = []
        for x in range(W):
            has_beam = False
            if grid[y][x] == '.' and x in beams: has_beam = True
            if x-1 >= 0 and grid[y][x-1] == '^' and x-1 in beams: has_beam = True
            if x+1 < W and grid[y][x+1] == '^' and x+1 in beams:
                has_beam = True
                sum += 1
            if has_beam:
                new_beams += [ x ]
        beams = new_beams

    print(filename, sum)
    return sum


assert(process("example.txt") == 21)
assert(process("input.txt") == 1598)
