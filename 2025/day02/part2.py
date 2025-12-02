#!/usr/bin/env python3

def isRepeating(val):
    for block_len in range(1, len(val)//2+1):
        if len(val) % block_len != 0: continue
        nr_blocks = len(val) // block_len
        if nr_blocks < 2: continue
        does_repeat = True
        for i in range(nr_blocks-1):
            if val[i*block_len:(i+1)*block_len] != val[(i+1)*block_len:(i+2)*block_len]:
                does_repeat = False
                break
        if does_repeat: return True
    return False

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

assert(process("example.txt") == 4174379265)
assert(process("input.txt") == 28915664389)
