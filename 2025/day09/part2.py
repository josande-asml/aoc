#!/usr/bin/env python3

import sys

def dump_grid(tiles,edge,ax=-1,ay=-1,bx=-1,by=-1):
    W = tiles[0][0]+1
    H = tiles[0][1]+1
    for (x,y) in tiles:
        if x+1 > W: W = x+1
        if y+1 > H: H = y+1

    left = min(ax,bx)
    right = max(ax,bx)
    top = min(ay,by)
    bottom = max(ay,by)

    print("")
    for y in range(H):
        for x in range(W):
            is_edge = False
            for (xx,yy,dxx,dyy) in edge:
                if xx == x and yy == y:
                    is_edge = True
                    dx = dxx
                    dy = dyy
                    break

            if x >= left and x <= right and y >= top and y <= bottom:
                print("O", end='')
            elif (x,y) in tiles:
                print("#", end='')
            elif is_edge:
                if dx == -1: print("^", end='')
                elif dx == +1: print("v", end='')
                elif dy == -1: print(">", end='')
                else: print("<", end='')
            else:
                print(".", end='')
        print("")

def process(filename):
    # Load tile coordinates
    tiles = []
    for line in open(filename):
        (x, y) = line.strip().split(',')
        tiles += [ (int(x), int(y)) ]

    # Calculate size of grid
    W = tiles[0][0]
    H = tiles[0][1]
    for (x,y) in tiles:
        W = max(W, x)
        H = max(H, y)
    W += 1
    H += 1

    # Calculate horizontal scan lines
    edge = []
    (x,y) = tiles[-1]
    for (xx,yy) in tiles:
        dx = 0
        if xx < x: dx = -1
        if xx > x: dx = +1
        dy = 0
        if yy < y: dy = -1
        if yy > y: dy = +1

        while x != xx or y != yy:
            x += dx
            y += dy
            if x != xx or y != yy:
                edge += [ (x,y,dx,dy) ]
            else:
                edge += [ (x,y,0,0) ]


    #dump_grid(tiles, edge)

    # Generate all possible rectangles that don't contain red
    # tiles within... (without more thorough checking yet)
    rects = []
    for i in range(len(tiles)-1):
        (ax,ay) = tiles[i]
        for j in range(len(tiles)):
            (bx,by) = tiles[j]
            is_valid = True
            for (x,y) in tiles:
                if x > min(ax,bx) and x < max(ax,bx) and \
                   y > min(ay,by) and y < max(ay,by):
                    is_valid = False
                    break
            if is_valid:
                area = (abs(ax-bx)+1)*(abs(ay-by)+1)
                rects += [ (area,ax,ay,bx,by) ]
    rects.sort(reverse=True)

    # Find the largests rectangle that is valid
    progress = 0
    print("Searching... {:5.2f}%".format(0.0), end='')
    for (area,ax,ay,bx,by) in rects:
        print("\b\b\b\b\b\b{:5.2f}%".format(progress/len(rects)), end='')
        sys.stdout.flush()
        progress += 1
        if is_valid_rect(edge,ax,ay,bx,by): break
    print("\b\b\b\b\b\bDone. ")

    print(filename, area)
    return area

# If there are red tiles inside the rectangle,
# then there will be boundary inside the rectangle
# so not all green tiles.
def is_valid_rect(edge,ax,ay,bx,by):
    left = min(ax,bx)
    right = max(ax,bx)
    top = min(ay,by)
    bottom = max(ay,by)

    for (x,y,dx,dy) in edge:
        if x >= left and x <= right and \
           y >= top and y <= bottom:
            if left != right:
                if x == left and dy == +1: return False
                if x == right and dy == -1: return False
            if top != bottom:
                if y == top and dx == -1: return False
                if y == bottom and dx == +1: return False
            if x > left and x < right and \
               y > top and y < bottom:
                return False
    return True

assert(process("example.txt") == 24)
assert(process("input.txt") == 1572047142)

