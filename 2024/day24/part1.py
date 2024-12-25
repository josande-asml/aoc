#!/usr/bin/env python3

def process(filename):
    f = open(filename)

    # load wire values
    wires = {}
    for line in f:
        line = line.strip()
        if len(line) == 0: break
        parts = line.split(': ')
        wires[parts[0]] = int(parts[1])

    # load gates
    gates = []
    for line in f:
        line = line.strip()
        parts = line.split()
        parts.remove("->")
        gates += [parts]

    # simulate gates
    hasChanged = True
    while hasChanged:
        hasChanged = False
        for gate in gates:
            a, oper, b, out = gate

            # already found output?
            if out in wires: continue

            # both inputs available?
            if a not in wires or b not in wires: continue

            # calculate gate
            if oper == "AND":
                wires[out] = (wires[a] & wires[b])
            elif oper == "OR":
                wires[out] = (wires[a] | wires[b])
            elif oper == "XOR":
                wires[out] = (wires[a] ^ wires[b])
            else:
                assert(False)
            hasChanged = True

    # calculate output Z
    z = 0
    for i in range(100):
        wire = "z{:02d}".format(i)
        if wire in wires:
            z |= (1 << i)*wires[wire]

    print(filename, z)
    return z


assert(process("example.txt") == 4)
assert(process("example2.txt") == 2024)
assert(process("input.txt") == 56278503604006)
