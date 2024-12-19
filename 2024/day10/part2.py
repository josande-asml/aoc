#!/usr/bin/env codon run

def checkTrail(grid, x, y, peaks):
   if grid[y][x] == 9:
      peaks += [ [ y, x ] ]
      return
   
   dirs = [ [ +1, 0 ], [ 0, +1 ], [ -1, 0 ], [ 0, -1 ] ]
   
   for dx, dy in dirs:
      if x+dx >= 0 and x+dx < len(grid[y]) and \
         y+dy >= 0 and y+dy < len(grid):
         if grid[y+dy][x+dx] == grid[y][x] + 1:
            checkTrail(grid, x+dx, y+dy, peaks)


#f = open('example.txt')
f = open('input.txt')

# Load grid
grid = []
for line in f:
   line = line.strip()
   row = []
   for c in line:
      row += [ int(c) ]
   grid += [ row ]

# Calculate trails
sum = 0
for y in range(len(grid)):
   for x in range(len(grid[y])):
      if grid[y][x] == 0:
         peaks = []
         checkTrail(grid, x, y, peaks)
         sum += len(peaks)

print(sum)  # 1816
