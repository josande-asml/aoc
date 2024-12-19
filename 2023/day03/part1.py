#!/usr/bin/env python3

def process(filename):
   grid = []
   for line in open(filename):
      line = line.strip()
      row = [ c for c in line ]
      grid += [ row ]
   H = len(grid)
   W = len(grid[0])

   sum = 0
   digits = ""
   for y in range(H):
      for x in range(W):
         c = grid[y][x]
         if c >= '0' and c <= '9':
            digits += grid[y][x]
         
         if x == W-1 or (c < '0' or c > '9'):
            if len(digits) > 0:
               hasSymbol = False
               for dy in range(-1, 2):
                  if y+dy < 0 or y+dy >= H: continue
                  for dx in range(-len(digits)-1, 1):
                     if x+dx < 0 or x+dx >= W: continue
                     c = grid[y+dy][x+dx]
                     if c != '.' and (c < '0' or c > '9'):
                        hasSymbol = True
               if hasSymbol:
                  sum += int(digits)
            digits = ""
   
   print(filename, sum)
   return sum
      
assert(process("example.txt") == 4361)
assert(process("input.txt") == 526404)
