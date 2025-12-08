#!/usr/bin/env python3
def process(filename, nr_connections):
    # Load coordinates
    coors = []
    for line in open(filename):
        parts = line.strip().split(',')
        coors += [ (int(parts[0]), int(parts[1]), int(parts[2])) ]
    N = len(coors)

    # Calculate sorted list of (squared) distances
    dists = []
    for i in range(N-1):
        (xi,yi,zi) = coors[i]
        for j in range(i+1, N):
            (xj,yj,zj) = coors[j]
            dist_sq = (xi-xj)*(xi-xj) + (yi-yj)*(yi-yj) + (zi-zj)*(zi-zj)
            dists += [ (dist_sq, i, j) ]
    dists.sort()

    # Create 10 connections
    circuits = []
    for n in range(nr_connections):
        (dist_sq, i, j) = dists[n]
        ci = False
        cj = False
        for m in range(len(circuits)):
            if i in circuits[m]: ci = m
            if j in circuits[m]: cj = m

        # i part of existing circuit, j is new --> add j to circuit
        if ci is not False and cj is False:
            circuits[ci] += [ j ]

        # j part of existing circuit, i is new --> add i to circuit
        elif ci is False and cj is not False:
            circuits[cj] += [ i ]

        # both part of existing circuit(s) --> ignore or merge circuits together
        elif ci is not False and cj is not False:
            if ci != cj:
                circuits[ci] += circuits[cj]
                circuits.pop(cj)

        # both not yet part of circuit --> begin a new circuit
        else:
            circuits += [ [ i, j ] ]

    # Calculate circuit lengths
    cirlens = []
    for circuit in circuits:
        cirlens += [ len(circuit) ]
    cirlens.sort(reverse=True)

    # Calculate product
    product = cirlens[0]*cirlens[1]*cirlens[2]
    print(filename, product)
    return product


assert(process("example.txt", 10) == 40)
assert(process("input.txt", 1000) == 352584)

