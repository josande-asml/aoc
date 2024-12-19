#!/usr/bin/env python3

#f = open('example.txt')
f = open('input.txt')

grid = []
for line in f:
   line = line.strip()
   row = []
   for c in line:
      row += [ c ]
   grid += [ row ]
H = len(grid)
W = len(grid[0])
   
antinodes = []
for y in range(H):
   row = []
   for x in range(W):
      row += [ '.' ]
   antinodes += [ row ]

for y in range(H):
   for x in range(W):
      if grid[y][x] != '.':
         antenna = grid[y][x]
         
         # search for identical antenna
         for yy in range(y, H):
            for xx in range(W):
               if y == yy and xx <= x: continue
               if grid[yy][xx] == antenna:
               
                  # found! add antinodes
                  dx = xx - x
                  dy = yy - y
                  
                  for i in range(H+W):
                     if y - i*dy >= 0 and y - i*dy < H and \
                        x - i*dx >= 0 and x - i*dx < W:
                        antinodes[y-i*dy][x-i*dx] = '#'
                           
                     if yy + i*dy >= 0 and yy + i*dy < H and \
                        xx + i*dx >= 0 and xx + i*dx < W:
                        antinodes[yy+i*dy][xx+i*dx] = '#'

for y in range(H):
   print("".join(grid[y]), "  ", "".join(antinodes[y]))

# count antinodes
count = 0
for y in range(H):
   for x in range(W):
      if antinodes[y][x] == '#':
         count += 1

print(count)  # 1287
