#!/usr/bin/env python3

graph = {}
count = 0

def find_path(node):
    global graph, count

    if node == "out":
        count += 1
    else:
        for branch in graph[node]:
            find_path(branch)


def process(filename):
    global graph, count

    graph = {}
    count = 0
    for line in open(filename):
        parts = line.strip().split(':')
        source = parts[0]
        targets = parts[1].strip().split(' ')
        graph[source] = targets

    find_path("you")

    print(filename, count)
    return count


assert(process("example.txt") == 5)
assert(process("input.txt") == 733)
