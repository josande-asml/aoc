#!/usr/bin/env python3
import sys
import copy

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
   print()


def dump2(grid):
   for row in grid:
      for col in row:
         print("{v:4d} ".format(v=col), end="")
      print()
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

   # Find best score
   worklist = []
   worklist += [[ 1, len(grid)-2, +1, 0, 0 ]]
   while len(worklist) > 0:
      x, y, dx, dy, score = worklist.pop()
      if grid[y][x] > 0 and grid[y][x] < score: continue  # already found shorter route
      if grid[y][x] < 0: continue  # wall
      grid[y][x] = score
      worklist += [[ x+dx, y+dy,  dx,  dy, score+1 ]]
      worklist += [[ x-dy, y+dx, -dy,  dx, score+1001 ]]
      worklist += [[ x+dy, y-dx,  dy, -dx, score+1001 ]]
   bestscore = grid[1][len(grid[0])-2]
   #print("bestscore =", bestscore)

   # Find all routes with same score    
   visited = []
   for y in range(len(grid)):
      row = [ 0 for x in range(len(grid[0])) ]
      visited += [ row ]
 
   worklist = []
   worklist += [[ 1, len(grid)-2, +1, 0, 0, [] ]]
   while len(worklist) > 0:
      x, y, dx, dy, score, route = worklist.pop()

      # are we walking in circles?
      if [x,y] in route: continue

      # walked into a wall?
      if grid[y][x] < 0: continue

      # are there more efficient routes? then abort search
      if score > grid[y][x] + 1001: continue 
      
      # reached the end?
      if x == len(grid[0])-2 and y == 1:
         if score == bestscore:
            for xx, yy in route:
               visited[yy][xx] = 1
         continue

      # try to make the next step from here
      worklist += [[ x+dx, y+dy,  dx,  dy, score+1,    route + [[x,y]] ]]
      worklist += [[ x-dy, y+dx, -dy,  dx, score+1001, route + [[x,y]] ]]
      worklist += [[ x+dy, y-dx,  dy, -dx, score+1001, route + [[x,y]] ]]
   #dump2(visited)

   # Count number of visited grid cells
   count = 1
   for row in visited:
      for col in row:
         count += col
   print("count =", count)
   return count


assert(process("example.txt") == 45)
assert(process("example2.txt") == 64)
assert(process("input.txt") == 511)

