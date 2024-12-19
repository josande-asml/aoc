#!/usr/bin/env python3

INTERACTIVE=False

def dump(grid):
   for row in range(len(grid)):
      print("".join(grid[row]))
   print()


def canBoxMove(grid, x, y, dx, dy):
   assert(grid[y][x] == '[' and grid[y][x+1] == ']')
   if dy == 0: # horizontal move
      if dx < 0:
         if   grid[y][x-1] == ']': return canBoxMove(grid, x-2, y, dx, dy)
         elif grid[y][x-1] == '.': return True
         elif grid[y][x-1] == '#': return False
         else: assert(False)
      else:
         if   grid[y][x+2] == '[': return canBoxMove(grid, x+2, y, dx, dy)
         elif grid[y][x+2] == '.': return True
         elif grid[y][x+2] == '#': return False
         else: assert(False)
         
   else: # vertical move
      if grid[y+dy][x] == '#' or grid[y+dy][x+1] == '#': return False
      if grid[y+dy][x] == '.' and grid[y+dy][x+1] == '.': return True
      if grid[y+dy][x] == '[': return canBoxMove(grid, x, y+dy, dx, dy)
      if grid[y+dy][x] == ']' and not canBoxMove(grid, x-1, y+dy, dx, dy): return False
      if grid[y+dy][x+1] == '[' and not canBoxMove(grid, x+1, y+dy, dx, dy): return False
      return True


def moveBox(grid, x, y, dx, dy):
   if dy == 0: # horizontal move
      if dx < 0 and grid[y][x-1] == ']': moveBox(grid, x-2, y, dx, dy)
      if dx > 0 and grid[y][x+2] == '[': moveBox(grid, x+2, y, dx, dy)
   else: # vertical move
      if grid[y+dy][x] == '[': moveBox(grid, x, y+dy, dx, dy)
      if grid[y+dy][x] == ']': moveBox(grid, x-1, y+dy, dx, dy)
      if grid[y+dy][x+1] == '[': moveBox(grid, x+1, y+dy, dx, dy)
   grid[y][x] = '.'
   grid[y][x+1] = '.'
   grid[y+dy][x+dx] = '['
   grid[y+dy][x+dx+1] = ']'


def process(filename):
   f = open(filename)

   # Load grid
   grid = []
   for line in f:
      line = line.strip()
      if line == "": break
      row = []
      for c in line:
         if c == '#':
            row += [ '#', '#' ]
         elif c == 'O':
            row += [ '[', ']' ]
         elif c == '.':
            row += [ '.', '.' ]
         elif c == '@':
            row += [ '@', '.' ]
         else:
            assert(False)
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
      elif grid[yy][xx] == ']':
         if canBoxMove(grid, xx-1, yy, dx, dy):
            moveBox(grid, xx-1, yy, dx, dy)
            x = xx
            y = yy
      elif grid[yy][xx] == '[':
         if canBoxMove(grid, xx, yy, dx, dy):
            moveBox(grid, xx, yy, dx, dy)
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
         if grid[row][col] == '[':
            sum += row*100 + col
   
   print(filename, "=", sum)
   return sum

assert(process("example2.txt") == 9021)
assert(process("input.txt") == 1512860)
