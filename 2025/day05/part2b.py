#!/usr/bin/env python3

def process(filename):
    # Load ranges
    overlapping_ranges = []
    for line in open(filename):
        line = line.strip()
        if line == '': break

        parts = line.split('-')
        x = int(parts[0])
        y = int(parts[1])

        overlapping_ranges += [ (x,y) ]

    # Merge overlapping ranges
    ranges = []
    y = False
    for (a, b) in sorted(overlapping_ranges):
        # does next range overlap current range?
        if y != False and a <= y:
            y = max(y, b)

        else:
            # emit last completed range
            if y != False:
                ranges += [ (x,y) ]

            # start a new range
            x = a
            y = b

	# emit last range
    ranges += [ (x,y) ]

    # Calculate number of fresh ingredients
    nr_fresh = 0
    for (a, b) in ranges:
        nr_fresh += b - a + 1

    print(filename, nr_fresh)
    return nr_fresh

assert(process("example.txt") == 14)
assert(process("input.txt") == 339668510830757)
