#!/usr/bin/env python3

def process(filename):
    sum = 0
    for line in open(filename):
        line = line.strip()
        max = 0
        for i in range(len(line)-1):
            for j in range(i+1, len(line)):
                if int(line[i])*10 + int(line[j]) > max:
                    max = int(line[i])*10 + int(line[j])
        sum += max

    print(filename, sum)
    return sum

assert(process("example.txt") == 357)
assert(process("input.txt") == 0)
