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

    nr_rolls_accessible = 0
    for y in range(H):
        for x in range(W):
            if grid[y][x] != '@': continue
            nr_neighbors = 0
            for yy in range(-1, 2):
                if y+yy < 0 or y+yy >= H: continue
                for xx in range(-1, 2):
                    if x+xx < 0 or x+xx >= W: continue
                    if xx == 0 and yy == 0: continue
                    if grid[y+yy][x+xx] == '@':
                        nr_neighbors += 1
            if nr_neighbors < 4:
                nr_rolls_accessible += 1

    print(filename, nr_rolls_accessible)
    return nr_rolls_accessible

assert(process("example.txt") == 13)
assert(process("input.txt") == 1451)

