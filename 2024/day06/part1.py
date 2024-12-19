import sys

# guard location and direction
x, y, dx, dy = 0, 0, 0, 0
grid = []

def findGuard(grid):
   global x, y, dx, dy
   for i in range(len(grid)):
      for j in range(len(grid[i])):
         if grid[i][j] == '^':
            x, y, dx, dy = j, i, 0, -1
            return
   sys.exit()


def step(grid):
   global x, y, dx, dy
   if x+dx < 0 or x+dx >= len(grid[0]): return False
   if y+dy < 0 or y+dy >= len(grid): return False
   if grid[y+dy][x+dx] == '#':
      dx, dy = -dy, dx
   else:
      grid[y][x] = 'X'
      x += dx
      y += dy
   return True


def dumpGrid(grid):
   for i in range(len(grid)):
      print("".join(grid[i]))
   print()


def countPositions(grid):
   count = 1
   for i in range(len(grid)):
      for j in range(len(grid[i])):
         if grid[i][j] == 'X':
            count += 1
   print(count)

   
#f = open('example.txt')
f = open('input.txt')
for line in f:
   line = line.strip()
   row = [ c for c in line ]
   grid += [ row ]

findGuard(grid)
#dumpGrid(grid)
while step(grid):
   #dumpGrid(grid)
   pass
   
countPositions(grid)  # 5153

