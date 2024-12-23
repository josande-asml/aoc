#!/usr/bin/env python3

import functools

# Key locations
numpad = {
    '7': (0, 0),
    '8': (1, 0),
    '9': (2, 0),
    '4': (0, 1),
    '5': (1, 1),
    '6': (2 ,1),
    '1': (0, 2),
    '2': (1, 2),
    '3': (2, 2),
    '0': (1, 3),
    'A': (2, 3),
    'X': (0, 3)
}

dirpad = {
    '^': (1, 0),
    'A': (2, 0),
    '<': (0, 1),
    'v': (1, 1),
    '>': (2, 1),
    'X': (0, 0)
}

# Generate steps needed to move from `src` to `dest`
# assumption, switching direction of movement costs time,
# so movement on numeric keyboard should be an angle, not
# a zigzag. This leaves only two options per move
def generateStep(src, dest, keypad):
    moves = []
    x, y = keypad[src]
    dx = keypad[dest][0] - keypad[src][0]
    dy = keypad[dest][1] - keypad[src][1]

    if (x + dx, y) != keypad['X']:
        seq = ""
        if dx > 0:
            seq = '>'*dx
        elif dx < 0:
            seq = '<'*-dx
        if dy > 0:
            seq += 'v'*dy
        elif dy < 0:
            seq += '^'*-dy
        moves += [ seq + 'A' ]

    if dx != 0 and dy != 0 and (x, y+dy) != keypad['X']:
        seq = ""
        if dy > 0:
            seq = 'v'*dy
        elif dy < 0:
            seq = '^'*-dy
        if dx > 0:
            seq += '>'*dx
        elif dx < 0:
            seq += '<'*-dx
        moves += [ seq + 'A' ]

    return moves


def findShortest(code, level, keypad, cache):
    if level == 0:
        return len(code)

    cacheKey = code + '/' + str(level)
    if cacheKey in cache:
        return cache[cacheKey]

    total = 0
    prev = 'A'
    for i in range(len(code)):
        moves = generateStep(prev, code[i], keypad)
        prev = code[i]
        shortest = -1
        for move in moves:
            length = findShortest(move, level-1, dirpad, cache)
            if shortest == -1 or length < shortest:
                shortest = length
        total += shortest

    cache[cacheKey] = total
    return total


def process(filename):
    cache = {}
    sum = 0
    for line in open(filename):
        code = line.strip()
        length = findShortest(code, 1+25, numpad, cache)
        number = int(code[:-1])
        sum += length * number

    print(filename, sum)
    return sum


assert(process("example.txt") == 154115708116294)
assert(process("input.txt") == 246810588779586)
