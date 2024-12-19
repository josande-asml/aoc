#!/usr/bin/env python3
import sys

def dump(grid):
   for row in grid:
      for col in row:
         if col == 0:
            print(".", end="")
         elif col > 0:
            print("*", end="")
         else:
            print("#", end="")
      print()


def process(filename):
   f = open(filename)

   # Load grid
   grid = []
   for line in f:
      line = line.strip()
      row = []
      for c in line:
         if c == '.' or c == 'S' or c == 'E':
            row += [ 0 ]
         else:
            row += [ -1 ]
      grid += [ row ]
   #dump(grid)

   worklist = []
   worklist += [[ 1, len(grid)-2, +1, 0, 0 ]]
   while len(worklist) > 0:
      x, y, dx, dy, score = worklist.pop()
      if grid[y][x] > 0 and grid[y][x] < score:
         continue
      if grid[y][x] < 0:
         continue
      grid[y][x] = score
      
      worklist += [[ x+dx, y+dy,  dx,  dy, score+1 ]]
      worklist += [[ x-dy, y+dx, -dy,  dx, score+1001 ]]
      worklist += [[ x+dy, y-dx,  dy, -dx, score+1001 ]]
     
   print("best score =", grid[1][len(grid[0])-2])
   return grid[1][len(grid[0])-2]


assert(process("example.txt") == 7036)
assert(process("example2.txt") == 11048)
assert(process("input.txt") == 95476)

