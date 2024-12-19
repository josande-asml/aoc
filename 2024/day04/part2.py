#f = open('example.txt')
f = open('input.txt')
grid = []
for line in f:
   line = line.strip()
   row = [ c for c in line ]
   grid += [ row ]
H = len(grid)
W = len(grid[0])

count = 0
for y in range(H-2):
   for x in range(W-2):
      if grid[y+1][x+1] == 'A' and \
         (grid[y][x]     == 'M' or grid[y][x]     == 'S') and \
         (grid[y][x+2]   == 'M' or grid[y][x+2]   == 'S') and \
         (grid[y+2][x]   == 'M' or grid[y+2][x]   == 'S') and \
         (grid[y+2][x+2] == 'M' or grid[y+2][x+2] == 'S'):
         if grid[y][x] != grid[y+2][x+2] and grid[y+2][x] != grid[y][x+2]:
            count += 1

print(count)  # 1890
