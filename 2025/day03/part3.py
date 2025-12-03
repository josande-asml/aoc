#!/usr/bin/env python3
# https://www.reddit.com/r/adventofcode/comments/1pddlmv/2025_day_3_part_3_caught_in_the_middle/

def find_max(line):
    left = 0
    right = len(line)
    number = ''
    for n in range(12):
        remaining_digits = 11-n
        max_digit = ''
        for i in range(left, right-remaining_digits):
            if line[i] > max_digit:
                max_digit = line[i]
                left = i+1
        number += max_digit
    return int(number)

def find_min(line):
    left = 0
    right = len(line)
    number = ''
    for n in range(12):
        remaining_digits = 11-n
        min_digit = ''
        for i in range(left, right-remaining_digits):
            if min_digit == '' or line[i] < min_digit:
                min_digit = line[i]
                left = i+1
        number += min_digit
    return int(number)

def find_closest(line, closest):
    index = []
    for i in range(12):
        index += [ i ]

    done = False
    best_error = False
    while True:
        number = ''
        for i in range(12):
            number += line[index[i]]
        if best_error == False or abs(int(number) - closest) < best_error:
            best_error = abs(int(number) - closest)
            best_number = int(number)
        if increase_counter(index, len(line)):
            break
    return best_number

def increase_counter(index, length):
    for i in range(11, -1, -1):
        index[i] += 1
        if index[i] < length-11+i:
            for j in range(i+1, 12):
                index[j] = index[j-1] + 1
            return False
    return True

def process(filename):
    sum = 0
    for line in open(filename):
        line = line.strip()
        max = find_max(line)
        min = find_min(line)
        avg = (max + min)//2
        closest = find_closest(line, avg)
        sum += closest
    print(filename, sum)
    return sum

assert(process("example.txt") == 2800777568611)

