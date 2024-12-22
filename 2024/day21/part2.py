#!/usr/bin/env python3

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


def generateNumMoves(code):
    moves = []
    code = 'A' + code       # start at 'A'
    for i in range(len(code)-1):
        stepMoves = generateStep(code[i], code[i+1], numpad)
        newMoves = []
        if len(moves) == 0:
            newMoves = stepMoves
        else:
            for m in moves:
                for sm in stepMoves:
                    newMoves += [ m + sm ]
        moves = newMoves
    return moves


def generateDirSeq(code):
    seq = ""
    code = 'A' + code       # start at 'A'
    for i in range(len(code)-1):
        stepMoves = generateStep(code[i], code[i+1], dirpad)
        seq += stepMoves[0]
    return seq


# Each move ends with a press of 'A'. After that
# the history/previous moves are no longer relevant.
# This means we can build up a cache and reuse sequences.
def findShortestSeqLength(code):
    shortestSeqLength = -1
    for move in generateNumMoves(code):
        # Break up move in parts from 'A' to 'A' and count
        # occurance of each sub-move type
        count = {}
        parts = move.split('A')[:-1]
        for part in parts:
            part += 'A'
            if part in count:
                count[part] += 1
            else:
                count[part] = 1

        # Repetitively expand sub-moves
        for n in range(25):
            count2 = {}
            for key, freq in count.items():
                seq = generateDirSeq(key)
                parts = seq.split('A')[:-1]
                for part in parts:
                    part += 'A'
                    if part in count2:
                        count2[part] += freq
                    else:
                        count2[part] = freq
            count = count2

        # Calculate sequence length
        length = 0
        for key, freq in count.items():
            length += freq*len(key)

        print(code, length)

        if shortestSeqLength == -1 or length < shortestSeqLength:
            shortestSeqLength = length

    return shortestSeqLength


def process(filename):
    sum = 0
    for line in open(filename):
        code = line.strip()
        seqLength = findShortestSeqLength(code)
        number = int(code[:-1])
        sum += seqLength * number

    print(filename, sum)
    return sum


assert(process("example.txt") == 175396398527088)
assert(process("input.txt") != 281309974290720)  # 281309974290720 is too high
                                                 # 112380591108802 is too low
