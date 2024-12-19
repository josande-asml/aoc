#!/usr/bin/env python3

INTERACTIVE=False

def dump(grid):
   for row in range(len(grid)):
      print("".join(grid[row]))
   print()


def moveBox(grid, x, y, dx, dy):
   assert(grid[y][x] == 'O')
   if grid[y+dy][x+dx] == '#': return False
   if grid[y+dy][x+dx] == 'O' and not moveBox(grid, x+dx, y+dy, dx, dy): return False
   assert(grid[y+dy][x+dx] == '.')
   grid[y+dy][x+dx] = 'O'
   grid[y][x] = '.'
   return True


def process(filename):
   f = open(filename)

   # Load grid
   grid = []
   for line in f:
      line = line.strip()
      if line == "": break
      row = [ c for c in line ]
      grid += [ row ]
   H = len(grid)
   W = len(grid[0])

   # Load moves
   moves = []
   for line in f:
      line = line.strip()
      moves += [ c for c in line ]

   # Find robot
   for r in range(H):
      for c in range(W):
         if grid[r][c] == '@':
            y = r
            x = c
            break

   # Simulate moves
   dirs = {
      '<': [ -1,  0 ],
      '^': [  0, -1 ],
      '>': [ +1,  0 ],
      'v': [  0, +1 ]
   }
   if INTERACTIVE:
      print("Initial state:")
      dump(grid)
   moveCount = 0
   for move in moves:
      dx, dy = dirs[move]
      grid[y][x] = '.'
      xx = x + dx
      yy = y + dy
      if grid[yy][xx] == '.':
         x = xx
         y = yy
      elif grid[yy][xx] == 'O':
         if moveBox(grid, xx, yy, dx, dy):
            x = xx
            y = yy
      elif grid[yy][xx] == '#':
         pass  
      else:
         assert(False)
      grid[y][x] = '@'

      if INTERACTIVE:
         moveCount += 1
         if moveCount > 0: #311:
            print("Move ", move, " (",moveCount,"/",len(moves),"):", sep="")
            dump(grid)
            input()
   
   # Calculate sum of position of boxes
   sum = 0
   for row in range(H):
      for col in range(W):
         if grid[row][col] == 'O':
            sum += row*100 + col

   print(filename, "=", sum)
   return sum

assert(process("example1.txt") == 2028)
assert(process("example2.txt") == 10092)
assert(process("input.txt") == 1492518)
