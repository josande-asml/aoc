#!/usr/bin/env python3
# https://www.reddit.com/r/adventofcode/comments/1pbqvw4/2025_day_1_part_3_use_the_right_method/

def process(filename):
    dial = 50
    nr_zeros = 0
    for line in open(filename):
        nr_clicks = int(line[1:])*0x434C49434B
        if line[0] == 'L':
            if nr_clicks >= 100:
                nr_zeros += nr_clicks // 100
                nr_clicks = nr_clicks % 100

            while nr_clicks > 0:
                nr_clicks -= 1
                if dial == 0:
                    dial = 99
                else:
                    dial -= 1
                    if dial == 0:
                        nr_zeros += 1
        elif line[0] == 'R':
            if nr_clicks >= 100:
                nr_zeros += nr_clicks // 100
                nr_clicks = nr_clicks % 100

            while nr_clicks > 0:
                nr_clicks -= 1
                if dial == 99:
                    dial = 0
                    nr_zeros += 1
                else:
                    dial += 1

    print(nr_zeros)
    return nr_zeros

assert(process("example.txt") == 1335377175147)
