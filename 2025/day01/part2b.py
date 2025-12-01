#!/usr/bin/env python3

def process(filename):
    dial = 50
    nr_zeros = 0
    for line in open(filename):
        nr_clicks = int(line[1:])
        if line[0] == 'L':
            dial = ((100-dial) % 100) + nr_clicks
            nr_zeros += dial//100
            dial = 100-dial
        else:
            dial += nr_clicks
            nr_zeros += dial//100
        dial = dial % 100

    print(nr_zeros)
    return nr_zeros

assert(process("example.txt") == 6)
assert(process("input.txt") == 5961)
