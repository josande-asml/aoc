#!/usr/bin/env python3

def find_paths(graph, node, dest):
    paths = {}
    for n in graph:
        paths[n] = -1
    return find_paths_iter(graph, paths, node, dest)


def find_paths_iter(graph, paths, node, dest):
    sum = 0
    for branch in graph[node]:
        if branch == dest:
            sum += 1
        elif branch == 'out':
            sum += 0
        else:
            if paths[branch] == -1:
                find_paths_iter(graph, paths, branch, dest)
            sum += paths[branch]
    paths[node] = sum
    return sum


def process(filename):
    graph = {'out':[]}
    for line in open(filename):
        parts = line.strip().split(':')
        source = parts[0]
        targets = parts[1].strip().split(' ')
        graph[source] = targets

    sum = \
        find_paths(graph, "svr", "dac") * \
        find_paths(graph, "dac", "fft") * \
        find_paths(graph, "fft", "out")

    sum += \
        find_paths(graph, "svr", "fft") * \
        find_paths(graph, "fft", "dac") * \
        find_paths(graph, "dac", "out")

    print(filename, sum)
    return sum


assert(process("example2.txt") == 2)
assert(process("input.txt") == 290219757077250)
