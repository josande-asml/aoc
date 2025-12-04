#!/usr/bin/env python3
# https://www.reddit.com/r/adventofcode/comments/1pdwr43/2025_day_4_part_3_islands_and_lakes/
import os.path

def process(filename):
    dir4 = [ (0,-1), (-1,0), (1,0), (0,1) ]
    dir8 = [ (-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1) ]

    # Load grid
    grid = []
    for line in open(filename):
        line = line.strip()
        row = [ c for c in line ]
        grid += [ row ]
    H = len(grid)
    W = len(grid[0])

    # Find islands
    islands = []
    for yy in range(H):
        for xx in range(W):
            if grid[yy][xx] == '@':
                island = []
                char = chr(ord('A') + len(islands))
                worklist = [ (xx,yy) ]
                while len(worklist) > 0:
                    (x,y) = worklist.pop(0)
                    if grid[y][x] == '@':
                        island += [ (x,y) ]
                        grid[y][x] = char

                        for (dx,dy) in dir8:
                            if x+dx >= 0 and x+dx < W and y+dy >= 0 and y+dy < H:
                                if grid[y+dy][x+dx] == '@':
                                    worklist += [ (x+dx,y+dy) ]
                #print(island)
                islands += [ island ]

    # Flood fill ocean from the edges inward
    for yy in range(H):
        for xx in range(W):
            if xx == 0 or xx == W-1 or yy == 0 or yy == H-1:
                if grid[yy][xx] == '.':
                    worklist = [ (xx,yy) ]
                    while len(worklist) > 0:
                        (x,y) = worklist.pop(0)
                        if grid[y][x] == '.':
                            grid[y][x] = ':'
                            for (dx,dy) in dir4:
                                if x+dx >= 0 and x+dx < W and y+dy >= 0 and y+dy < H:
                                    if grid[y+dy][x+dx] == '.':
                                        worklist += [ (x+dx,y+dy) ]

    # Dump resulting map
    filename = 'islands.txt'
    with open(filename, 'w') as fp:
        for y in range(H):
            for x in range(W):
                fp.write(grid[y][x])
            fp.write("\n")
    print("Written \"{:s}\"".format(filename))

    # Check for lakes adjacent to islands
    nr_islands_with_lake = 0
    char = 'A'
    for island in islands:
        found_lake = False
        for (x,y) in island:
            for (dx,dy) in dir4:
                if x+dx >= 0 and x+dx < W and y+dy >= 0 and y+dy < H:
                    if grid[y+dy][x+dx] == '.':
                        found_lake = True
        if found_lake:
            nr_islands_with_lake += 1
            print("Island {:s} has a lake".format(char))

        char = chr(ord(char) + 1)

    print(nr_islands_with_lake)
    return nr_islands_with_lake

if not os.path.isfile('output.txt'):
    print("Please run part2.py first to generate output.txt")
else:
    assert(process("output.txt") == 10)
