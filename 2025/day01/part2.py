#!/usr/bin/env python3

def process(filename):
    dial = 50
    nr_zeros = 0
    for line in open(filename):
        nr_clicks = int(line[1:])
        if line[0] == 'L':
            if dial == 0: dial = 100
            while nr_clicks >= dial:
                nr_clicks -= dial
                dial = 100
                nr_zeros += 1
            dial -= nr_clicks
            if dial == 100: dial = 0
        elif line[0] == 'R':
            while nr_clicks >= 100-dial:
                nr_clicks -= 100-dial
                dial = 0
                nr_zeros += 1
            dial += nr_clicks
    print(nr_zeros)
    return nr_zeros

assert(process("example.txt") == 6)
assert(process("input.txt") == 5961)
