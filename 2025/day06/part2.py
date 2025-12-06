#!/usr/bin/env python3
import re

def process(filename):
    # Determine maximum width
    W = 0
    for line in open(filename):
        if len(line.rstrip()) > W:
            W = len(line.rstrip())

    # Load lines and add padding to the right
    grid = []
    strfmt = "{:" + str(W)+  "}"
    for line in open(filename):
        grid += [ strfmt.format(line.rstrip()) ]
    H = len(grid)

    # Process problems
    sum = 0
    left = 0
    while left < W:
        # Isolate the vertical strip with the problem
        right = left+1
        while right < W:
            found_separator = True
            for y in range(H):
                if grid[y][right] != ' ':
                    found_separator = False
            if found_separator:
                break
            else:
                right += 1

        # Calculate problem
        operator = grid[H-1][left:right].strip()
        answer = False
        for x in range(left, right):
            number = ''
            for y in range(H-1):
                number += grid[y][x]
            if answer == False:
                answer = int(number.strip())
            else:
                if operator == '+':
                    answer += int(number.strip())
                else:
                    answer *= int(number.strip())
        sum += answer

        # Move to next vertical strip
        left = right+1

    print(filename, sum)
    return sum


assert(process("example.txt") == 3263827)
assert(process("input.txt") == 7903168391557)
