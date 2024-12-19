#!/usr/bin/env python3 

#f = open('example3.txt')
f = open('input.txt')

dirs = [ [ -1, 0 ], [ 0, -1 ], [ +1, 0 ], [ 0, +1] ]
 
def dump():
   for y in range(H):
      for x in range(W):
         print("{id:3d} ".format(id = regions[y][x]), end="")
      print()

def fill(y, x, id):
   regions[y][x] = id
   for dx, dy in dirs:
      if x+dx >= 0 and x+dx < W and y+dy >= 0 and y+dy < H:
         if regions[y+dy][x+dx] == -1 and grid[y+dy][x+dx] == grid[y][x]:
            fill(y+dy, x+dx, id)

# Load grid
grid = []
for line in f:
   line = line.strip()
   row = [ c for c in line ]
   grid += [ row ]
H = len(grid)
W = len(grid[0])

# Number regions
regions = []
for y in range(H):
   row = []
   for x in range(W):
      row += [ -1 ]
   regions += [ row ]

id = 0
for y in range(H):
   for x in range(W):
      if regions[y][x] == -1:
         fill(y, x, id)
         id += 1
#dump()

# Calculate area and perimeter
area = [ 0 for i in range(id) ]
perimeter = [ 0 for i in range(id) ]
for y in range(H):
   for x in range(W):
      area[regions[y][x]] += 1
      for dx, dy in dirs:
         if x+dx >= 0 and x+dx < W and y+dy >= 0 and y+dy < H:
            if regions[y+dy][x+dx] != regions[y][x]:
               perimeter[regions[y][x]] += 1
         else:
            perimeter[regions[y][x]] += 1

#print(area)
#print(perimeter)

# Calculate cost
cost = 0
for i in range(id):
   cost += area[i] * perimeter[i]

print(cost)

