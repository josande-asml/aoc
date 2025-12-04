#!/usr/bin/env python3
# https://www.reddit.com/r/adventofcode/comments/1pbqvw4/2025_day_1_part_3_use_the_right_method/

def process(filename):
    dial = 50
    nr_zeros = 0
    for line in open(filename):
        nr_clicks = int(line[1:])*0x434C49434B
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

assert(process("example.txt") == 1335377175147)
