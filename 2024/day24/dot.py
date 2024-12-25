#!/usr/bin/env python3
# $ python3 dot.py > dot.txt
# $ dot -Tsvg dot.txt -o dot.svg

f = open("input.txt")

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

print("digraph {")
for gate in gates:
    print("   ",gate[0], "->", gate[3])
    print("   ",gate[2], "->", gate[3])
print("}")
