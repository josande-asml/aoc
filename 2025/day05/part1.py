#!/usr/bin/env python3

def process(filename):
    with open(filename) as fp:
        fresh_ranges = []
        while (line := fp.readline()) != '':
            line = line.strip()
            if line == '': break
            (a, b) = line.split('-')
            fresh_ranges += [ (int(a), int(b)) ]

        nr_fresh = 0
        while (line := fp.readline()) != '':
            ingredient = int(line.strip())
            for (a, b) in fresh_ranges:
                if ingredient >= a and ingredient <= b:
                    nr_fresh += 1
                    break

    print(filename, nr_fresh)
    return nr_fresh


assert(process("example.txt") == 3)
assert(process("input.txt") == 513)
