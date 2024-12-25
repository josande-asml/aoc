#!/usr/bin/env python3

# Our assumption is that when we have a partially correct solution,
# then a part of the output bits will also be correct. This implies
# we can converge towards a correct solution by reusing parts of the
# partial solution.
#
# First we create a list of randomly generated swap patterns. This is
# our first "generation".
#
# Next we grow a new generation using these operations (retrying each
#  time we get a duplicate that is already in the generation):
#
# - in 60% of the cases we randomly select two swap patterns and create
#   a new swap pattern by randomy using pieces either two.
#
# - in 30% of the cases we randomly select a swap pattern and replace
#   one of the swap by a new random swap.
#
# - in 10% of the cases we generate a completely new random swap pattern.
#
# The new generation is much larger that the old generation. For each
# swap pattern we calculate the number of invalid output bits. We select
# the best swap patterns from the new generation and start the next
# iteration.
#
# This algorithm does converge very slowly and might not ever find the
# solution. When we noticed this, we started coding the exhaustive search
# method below.

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
    samples += [(0, 0)]
    samples += [((1 << nrBits)-1, 0)]
    samples += [(0, (1 << nrBits)-1)]
    samples += [((1 << nrBits)-1, (1 << nrBits)-1)]

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


def dump(generation, genCount):
    sum = 0
    for g in generation:
        sum += g[0]
    avg = sum/len(generation)

    f = open("converge.csv", "a")
    f.write("{:.6f}\n".format(avg))
    f.close()

    print("Generation #", genCount, " ({:.6f}):".format(avg), sep="")
    for g in generation:
        print("   {:.6f}".format(g[0]), g[1])
    print()


def isValidSwap(generation, swaps):
    # make sure swaps are sorted and valid
    for (a,b) in swaps:
        if a >= b: return False

    # make sure we don't swap same output twice
    for i in range(len(swaps)-1):
        for j in range(i+1, len(swaps)):
            if swaps[i][0] == swaps[j][0] or \
               swaps[i][0] == swaps[j][1] or \
               swaps[i][1] == swaps[j][0] or \
               swaps[i][1] == swaps[j][1]: return False

    # make sure swap is not already in generation
    duplicate = False
    for g in generation:
        if all((t in g[1]) for t in swaps):
            duplicate = True
    return not duplicate


# Try to find out what gates have been swapped by randomly
# selecting gates and see if that improves the average number
# of invalid bits
def findSwaps(gates, nrBits, nrSwaps, samples, oper):
    genSize = int(math.sqrt(len(gates)))   # number of attempts per generation

    # create (arbitrary) first generation
    print("Root generation:")
    generation = []
    for n in range(genSize):
        while True:
            swaps = []
            for i in range(nrSwaps):
                while True:
                    a = random.randrange(len(gates))
                    b = random.randrange(len(gates))
                    if a > b: a,b = b,a
                    if a == b: continue
                    if any(a in t for t in swaps): continue
                    if any(b in t for t in swaps): continue
                    swaps += [ (a,b) ]
                    break

            swaps = sorted(swaps)
            if isValidSwap(generation, swaps): break

        nrErrors = calcNrErrors(gates, nrBits, swaps, samples, oper)
        generation += [ (nrErrors, swaps) ]
        #print("   {:.6f}".format(nrErrors), swaps)

    generation = sorted(generation)
    genCount = 0
    dump(generation, genCount)

    # mix and mutate generation to create next generation
    while True:
        if generation[0][0] == 0.0:     # found the solution!
            print("Solution:", generation[0])
            return generation[0][1]

        nextGen = copy.deepcopy(generation)
        for n in range(10*genSize):
            while True:
                rand = random.random()
                if rand < 0.6:
                    # cross genes A and B
                    ga = random.randrange(len(generation))
                    while True:
                        gb = random.randrange(len(generation))
                        if ga != gb: break
                    #print("a  :", generation[ga][1])
                    #print("b  :", generation[gb][1])

                    swaps = []
                    for i in range(nrSwaps):
                        if random.random() < 0.5:
                            swaps += [ generation[ga][1][i] ]
                        else:
                            swaps += [ generation[gb][1][i] ]
                    #print("a+b:", swaps)
                elif rand < 0.9:
                    # mutate gene
                    ga = random.randrange(len(generation))
                    swaps = copy.deepcopy(generation[ga][1])
                    #print("a  :", swaps)
                    i = random.randrange(nrSwaps)
                    while True:
                        a = random.randrange(len(gates))
                        b = random.randrange(len(gates))
                        if a > b: a,b = b,a
                        if a == b: continue
                        if any(a in t for t in swaps): continue
                        if any(b in t for t in swaps): continue
                        swaps[i] = (a,b)
                        break
                    #print("a* :", swaps)
                else:
                    swaps = []
                    for i in range(nrSwaps):
                        while True:
                            a = random.randrange(len(gates))
                            b = random.randrange(len(gates))
                            if a > b: a,b = b,a
                            if a == b: continue
                            if any(a in t for t in swaps): continue
                            if any(b in t for t in swaps): continue
                            swaps += [ (a,b) ]
                            break

                swaps = sorted(swaps)
                if isValidSwap(nextGen, swaps): break

            nrErrors = calcNrErrors(gates, nrBits, swaps, samples, oper)
            nextGen += [ (nrErrors, swaps) ]

        generation = sorted(nextGen)
        generation = generation[0:genSize]
        genCount += 1
        dump(generation, genCount)


def process(filename, nrBits, nrSwaps, oper):
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
    print("Loaded", len(gates), "gates")

    # try to find swapped gates
    samples = generateSamples(20, nrBits)
    swaps = findSwaps(gates, nrBits, nrSwaps, samples, oper)

    # find names of outputs to swap
    outs = []
    for (a,b) in swaps:
        outs += [ gates[a][3] ]
        outs += [ gates[b][3] ]
    outs = ",".join(sorted(outs))

    print(filename, outs)
    return outs


assert(process("example3.txt", 6, 2, 'and') == "z00,z01,z02,z05")
assert(process("input.txt",   45, 4, 'add') == "bhd,brk,dhg,dpd,nbf,z06,z23,z38")
