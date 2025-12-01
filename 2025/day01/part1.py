#!/usr/bin/env python3

def process(filename):
    dial = 50
    nr_zeros = 0
    for line in open(filename):
        if   line[0] == 'R': dial = (dial - int(line[1:])) % 100
        elif line[0] == 'L': dial = (dial + int(line[1:])) % 100
        else:
            print('Invalid input')
            exit()
        if dial == 0: nr_zeros += 1
    print(nr_zeros)
    return nr_zeros

assert(process("example.txt") == 3)
assert(process("input.txt") == 980)
