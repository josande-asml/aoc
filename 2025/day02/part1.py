#!/usr/bin/env python3

def isRepeating(val):
    l = len(val)
    if l % 2 != 0: return False
    return val[0:l//2] == val[l//2:]

def process(filename):
    sum = 0
    for line in open(filename):
        parts = line.strip().split(',')
        for part in parts:
            (a, b) = part.split('-')
            a = int(a)
            b = int(b)
            for x in range(a, b+1):
                if isRepeating(str(x)):
                    sum += x

    print(filename, sum)
    return sum

assert(process("example.txt") == 1227775554)
assert(process("input.txt") == 21898734247)
