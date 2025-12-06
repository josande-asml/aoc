#!/usr/bin/env python3
# From: https://www.reddit.com/r/adventofcode/comments/1peyw7w/2025_day_5_part_3_superfresh_ingredients/

def process(filename):
    # Load ranges from file
    with open(filename) as fp:
        ranges = []
        while (line := fp.readline()) != '':
            line = line.strip()
            if line == '': break
            (a, b) = line.split('-')
            ranges += [ (int(a), int(b)) ]

    # Find overlapping ranges
    overlap = []
    for i in range(len(ranges)-1):
        (a,b) = ranges[i]
        for j in range(i+1, len(ranges)):
            (c,d) = ranges[j]

            # (a,b) totally inside (c,d)
            #      [a===b]
            #   [c==========d]
            if a >= c and b <= d:
                overlap += [ (a,b) ]

            # (a,b) overlaps on right side with (c,d)
            #   [a======b]
            #         [c=====d]
            elif a < c and b > c and b <= d:
                overlap += [ (c, b) ]

            # (a,b) overlaps on left side with (c,d)
            #        [a======b]
            #   [c=====d]
            elif b > d and a < d and a >= c:
                overlap += [ (a, d) ]

            # (a,b) totally overspans (c,d)
            #   [a===========b]
            #      [c====d]
            elif a <= c and b >= d:
                overlap += [ (c,d) ]

    # Calculate number of fresh ingredients
    nr_fresh = 0
    for (a, b) in overlap:
        nr_fresh += b - a + 1

    print(filename, nr_fresh)
    return nr_fresh


assert(process("example.txt") == 6)
assert(process("input.txt") == 98261601491701)
