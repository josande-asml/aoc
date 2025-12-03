#!/usr/bin/env python3

def process(filename):
    sum = 0
    for line in open(filename):
        left = 0
        right = len(line.strip())
        number = ''
        for n in range(12):
            remaining_digits = 11-n
            max_digit = ''
            for i in range(left, right-remaining_digits):
                if line[i] > max_digit:
                    max_digit = line[i]
                    left = i+1
            number += max_digit
        sum += int(number)

    print(filename, sum)
    return sum

assert(process("example.txt") == 3121910778619)
assert(process("input.txt") == 171518260283767)

