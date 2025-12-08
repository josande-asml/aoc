#!/usr/bin/env python3
def process(filename):
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

    # Create connections until we have 1 large circuit
    circuits = []
    for (dist_sq, i, j) in dists:
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

        if len(circuits) == 1 and len(circuits[0]) == N:
            product = coors[i][0] * coors[j][0]
            break

    print(filename, product)
    return product


assert(process("example.txt") == 25272)
assert(process("input.txt") == 9617397716)

