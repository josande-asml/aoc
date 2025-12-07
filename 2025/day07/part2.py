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

    # Init beam counter
    nr_beams = []
    for x in range(W):
        nr_beams += [ 0 ]

    # Find starting point
    for x in range(W):
        if grid[0][x] == 'S':
            nr_beams[x] = 1
            break

    # Simulate beam splitting
    for y in range(2, H-1, 2):
        new_nr_beams = []
        for x in range(W):
            new_nr_beams += [ 0 ]

        for x in range(W):
            if grid[y][x] == '.':
                new_nr_beams[x] += nr_beams[x]

            if x-1 >= 0 and grid[y][x-1] == '^':
                new_nr_beams[x] += nr_beams[x-1]

            if x+1 < W and grid[y][x+1] == '^':
                new_nr_beams[x] += nr_beams[x+1]

        nr_beams = new_nr_beams

    print(filename, sum(nr_beams))
    return sum(nr_beams)


assert(process("example.txt") == 40)
assert(process("input.txt") == 4509723641302)
