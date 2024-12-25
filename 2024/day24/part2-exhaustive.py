#!/usr/bin/env python3

# Our assumption is that when we have a partially correct solution,
# then a part of the output bits will also be correct. This implies
# we can converge towards a correct solution by reusing parts of the
# partial solution.
#
# We exhaustively search all combinations of two gates to swap and
# measure which pair gives the lowest number of invalid output bits.
# We keep the best pair, and start searching for the second pair by
# again measuring the number of invalid output bits.
#
# We keep adding pairs until we have the right amount of pairs. If
# that was not yet the solution, we remove the oldest pair and try
# to add a new pair.

import random
import math
import copy

def simulate(wires, gates):
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


def generateSamples(nrSamples, nrBits):
    samples = []

    # test patterns using: 0101010101 and 1010101010
    odd = 0
    even = 0
    for i in range(nrBits):
        if (i & 1) == 0:
            even |= (1 << i)
        else:
            odd |= (1 << i)
    samples += [(odd, odd)]
    samples += [(odd, even)]
    samples += [(even, odd)]
    samples += [(even, even)]

    # test patterns using: 0000000000 and 1111111111
    samples += [(0, 0)]
    samples += [((1 << nrBits)-1, 0)]
    samples += [(0, (1 << nrBits)-1)]
    samples += [((1 << nrBits)-1, (1 << nrBits)-1)]

    # test patterns using random bits
    random.seed(1)  # always use same "random" numbers for reproducibility of bugs/convergence
    for n in range(nrSamples-8):
        x = random.randrange(1 << nrBits)
        y = random.randrange(1 << nrBits)
        samples += [(x, y)]

    return samples


# Calculate number of invalid output bits
def calcNrErrors(gates, nrBits, swaps, samples, oper):
    for (a, b) in swaps:
        gates[a][3], gates[b][3] = gates[b][3], gates[a][3]

    nrErrors = 0
    for (x, y) in samples:
        if oper == 'and':
            z = x & y
        elif oper == 'add':
            z = x + y
        else:
            assert(False)

        wires = {}
        for i in range(nrBits):
            wires["x{:02d}".format(i)] = ((x >> i) & 1)
            wires["y{:02d}".format(i)] = ((y >> i) & 1)

        simulate(wires, gates)

        for i in range(nrBits):
            out = "z{:02d}".format(i)
            if out not in wires or wires[out] != ((z >> i) & 1):
                nrErrors += 1

        out = "z{:02d}".format(nrBits)  # challenge has 1 extra bit compared to example
        if out in wires and wires[out] != ((z >> nrBits) & 1):
            nrErrors += 1

    for (a, b) in swaps:
        gates[a][3], gates[b][3] = gates[b][3], gates[a][3]

    return nrErrors / len(samples)


# Search for best pair to swap
def findSwaps(gates, nrBits, nrSwaps, samples, oper):
    base = []
    while len(base) < nrSwaps:
        print("\nSearching for pair #", len(base)+1, sep="")
        bestSwaps = None
        bestNrErrors = -1
        for a in range(len(gates)-1):
            if any(a in t for t in base): continue
            for b in range(a+1, len(gates)):
                if any(b in t for t in base): continue
                swap = (a,b)
                swaps = base + [ swap ]
                nrErrors = calcNrErrors(gates, nrBits, swaps, samples, oper)
                if nrErrors == 0:
                    print("Solution:", swaps)
                    return swaps
                if nrErrors < bestNrErrors or bestSwaps == None:
                    bestSwaps = swaps
                    bestNrErrors = nrErrors
                    print("   {:.6f}".format(bestNrErrors), bestSwaps)
        base = bestSwaps

        if len(base) == nrSwaps:
            base.pop(0)

    print("ERROR: Solution not found!")
    return base;


def process(filename, nrBits, nrSwaps, errorFunc):
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

    # try to find swapped gates
    samples = generateSamples(20, nrBits)
    swaps = findSwaps(gates, nrBits, nrSwaps, samples, errorFunc)

    # find names of outputs to swap
    # solution: [(60, 128), (41, 189), (120, 138), (9, 160)]
    outs = []
    for (a,b) in swaps:
        outs += [ gates[a][3] ]
        outs += [ gates[b][3] ]
    outs = ",".join(sorted(outs))

    print(filename, outs)
    return outs


assert(process("example3.txt", 6, 2, 'and') == "z00,z01,z02,z05")
assert(process("input.txt",   45, 4, 'add') == "bhd,brk,dhg,dpd,nbf,z06,z23,z38")
