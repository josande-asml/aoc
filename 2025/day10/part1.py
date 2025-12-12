#!/usr/bin/env python3

def is_valid(counts, lights, buttons):
    state = [ 0 ] * len(lights)
    for j in range(len(counts)):
        for but in buttons[j]:
            state[but] ^= (counts[j] % 2)

    for j in range(len(lights)):
        if lights[j] == '.' and state[j] != 0: return False
        if lights[j] == '#' and state[j] != 1: return False
    return True

def solve(machine):
    (lights, buttons, joltage) = machine
    min_nr_presses = len(buttons)
    for n in range(1 << len(buttons)):
        counts = [0] * len(buttons)
        nr_presses = 0
        for m in range(len(buttons)):
            bitmask = 1 << m
            if (n & bitmask) > 0:
                counts[m] = 1
                nr_presses += 1
        if is_valid(counts, lights, buttons):
            if nr_presses < min_nr_presses:
                min_nr_presses = nr_presses
    return min_nr_presses

def process(filename):
    # Load puzzle
    machines = []
    for line in open(filename):
        parts = line.strip().split(' ')
        lights = parts[0][1:-1]
        buttons = []
        for but in parts[1:-1]:
            wiring = []
            for wire in but[1:-1].split(','):
                wiring += [ int(wire) ]
            buttons += [ wiring ]
        joltage = parts[-1]
        machines += [ (lights, buttons, joltage) ]

    # Brute-force solutions
    sum = 0
    for machine in machines:
        ans = solve(machine)
        #print(machine, ans)
        sum += ans

    print(filename, sum)
    return sum


assert(process("example.txt") == 7)
assert(process("input.txt") == 415)
