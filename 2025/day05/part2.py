#!/usr/bin/env python3

def add_range(ranges, x, y):
    # See if new (x,y) can be merged with existing range
    new_ranges = []
    is_merged = False
    for (a,b) in ranges:
        # new range fits fully inside existing range,
        # ignore new range
        if x >= a and y <= b:
            is_merged = True

        # new range overlaps on left side of existing range
        if x < a and y+1 >= a:
            a = x
            b = max(b, y)
            is_merged = True

        # new range overlaps on right side of existing range
        if y > b and x-1 <= b:
            b = y
            a = min(a, x)
            is_merged = True

        new_ranges += [ (a,b) ]

    if not is_merged:
        new_ranges += [ (x,y) ]

    if is_merged:
        # ranges have changed. Rerun again because more ranges might now overlap
        ranges.clear()
        for (a,b) in new_ranges:
            add_range(ranges, a, b)
    else:
        # Copy resulting new ranges to output
        ranges.clear()
        for (a,b) in new_ranges:
            ranges += [ (a,b) ]


def process(filename):
    ranges = []
    for line in open(filename):
        line = line.strip()
        if line == '': break

        parts = line.split('-')
        x = int(parts[0])
        y = int(parts[1])

        add_range(ranges, x, y)

    # Calculate number of fresh ingredients
    nr_fresh = 0
    for (a, b) in ranges:
        nr_fresh += b - a + 1

    print(filename, nr_fresh)
    return nr_fresh

assert(process("example.txt") == 14)
assert(process("input.txt") == 339668510830757)
