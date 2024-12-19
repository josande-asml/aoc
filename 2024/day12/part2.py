#!/usr/bin/env python3 

def dump(regions, W, H):
   for y in range(H+2):
      for x in range(W+2):
         print("{id:3d} ".format(id = regions[y][x]), end="")
      print()

def fill(grid, regions, y, x, id):
   dirs = [ [ -1, 0 ], [ 0, -1 ], [ +1, 0 ], [ 0, +1] ]
   regions[y][x] = id
   for dx, dy in dirs:
      if regions[y+dy][x+dx] == -1 and grid[y+dy][x+dx] == grid[y][x]:
         fill(grid, regions, y+dy, x+dx, id)

def process(filename):
   # Load grid
   f = open(filename)
   grid = []
   for line in f:
      line = line.strip()
      row = [ c for c in line ]
      grid += [ row ]
   H = len(grid)
   W = len(grid[0])

   # Expand border around grid
   newgrid = []
   newgrid += [ [ '#' for i in range(W+2) ] ]
   for row in grid:
      row.insert(0, '#')
      row.append('#')
      newgrid += [ row ]
   newgrid += [ [ '#' for i in range(W+2) ] ]
   grid = newgrid

   # Assign numbers to regions
   regions = []
   regions += [ [ -2 for i in range(W+2) ] ]
   for y in range(H):
      row = [ -2 ]
      for x in range(W):
         row += [ -1 ]
      row += [ -2 ]
      regions += [ row ]
   regions += [ [ -2 for i in range(W+2) ] ]

   id = 0
   for y in range(1, H+1):
      for x in range(1, W+1):
         if regions[y][x] == -1:
            fill(grid, regions, y, x, id)
            id += 1
   #dump(regions, W, H)

   # Calculate area 
   area = [ 0 for i in range(id) ]
   for y in range(1, H+1):
      for x in range(1, W+1):
         area[regions[y][x]] += 1
   #print(area)

   # Calculate perimeter
   perimeter = [ [] for i in range(id) ]
   for y in range(1, H+2):
      for x in range(1, W+2):
         
         if regions[y-1][x] != regions[y][x]:
            if regions[y][x] >= 0:
               perimeter[regions[y][x]] += [ [x, y, 'H'] ]
            if regions[y-1][x] >= 0:
               perimeter[regions[y-1][x]] += [ [x, y, 'h'] ]
            
         if regions[y][x-1] != regions[y][x]:
            if regions[y][x] >= 0:
               perimeter[regions[y][x]] += [ [x, y, 'V'] ]
            if regions[y][x-1] >= 0:
               perimeter[regions[y][x-1]] += [ [x, y, 'v'] ]
            
   # Calculate number of sides
   sides = [ 0 for i in range(id) ]
   for i in range(id):
      for j in range(len(perimeter[i])):
         x, y, d = perimeter[i][j]
      
         found = False
         for k in range(j):
            if d.upper() == 'H' and perimeter[i][k] == [x-1, y, d] or \
               d.upper() == 'H' and perimeter[i][k] == [x+1, y, d] or \
               d.upper() == 'V' and perimeter[i][k] == [x, y-1, d] or \
               d.upper() == 'V' and perimeter[i][k] == [x, y+1, d]:
               found = True
         
         if not found:
            sides[i] += 1

   # Calculate cost
   cost = 0
   for i in range(id):
      cost += area[i] * sides[i]
   return cost

assert(process("example1.txt") == 80)
assert(process("example2.txt") == 436)
assert(process("example3.txt") == 1206)
assert(process("example4.txt") == 236)
assert(process("example5.txt") == 368)

print(process("input.txt"))  # 818286


