#!/usr/bin/env python3

def addLockOrKey(locks, keys, grid):
    if grid[0] == '#####':
        lock = [ 0, 0, 0, 0, 0 ]
        for y in range(1, 6):
            for x in range(5):
                if grid[y][x] == '#':
                    lock[x] = y
        locks += [lock]
    elif grid[6] == '#####':
        key = [ 0, 0, 0, 0, 0 ]
        for y in range(1, 6):
            for x in range(5):
                if grid[6-y][x] == '#':
                    key[x] = y
        keys += [key]
    else:
        assert(False)  # lock nor key


def process(filename):
    # Load input file
    locks = []
    keys = []
    grid = []
    for line in open(filename):
        line = line.strip()
        if len(line) > 0:
            grid += [line]
        else:
            addLockOrKey(locks, keys, grid)
            grid = []
    addLockOrKey(locks, keys, grid)

    # Try combinations
    nrFits = 0
    for lock in locks:
        for key in keys:
            doesFit = True
            for i in range(5):
                if lock[i]+key[i] > 5:
                    doesFit = False
            if doesFit:
                nrFits += 1

    print(filename, nrFits)
    return nrFits


assert(process("example.txt") == 3)
assert(process("input.txt") == 3196)
