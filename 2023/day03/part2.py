#!/usr/bin/env python3

# Extract number of which one of the digits is at grid[y][x]
def getNumber(grid, x, y):
   digits = ""
   if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid): return False
   if grid[y][x] < '0' or grid[y][x] > '9': return False

   left = x
   while left-1 >= 0 and \
      grid[y][left-1] >= '0' and grid[y][left-1] <= '9': left -= 1
   right = x
   while right+1 < len(grid[y]) and \
      grid[y][right+1] >= '0' and grid[y][right+1] <= '9': right += 1

   digits = ""
   for x in range(left, right+1):
      digits += grid[y][x]
   return int(digits)


# Try to extra number at grid[y][x]. If successful add to `numbers`
# list. Returns True if success, False if no number found.
def addNumber(numbers, grid, x, y):
   a = getNumber(grid, x, y)
   if a:
      numbers += [ a ]
      return True      
   return False


def process(filename):
   grid = []
   for line in open(filename):
      line = line.strip()
      row = [ c for c in line ]
      grid += [ row ]
   H = len(grid)
   W = len(grid[0])

   sum = 0
   for y in range(H):
      for x in range(W):
         if grid[y][x] == '*':
            numbers = []
            if not addNumber(numbers, grid, x, y-1):
               addNumber(numbers, grid, x-1, y-1)
               addNumber(numbers, grid, x+1, y-1)
            addNumber(numbers, grid, x-1, y)
            addNumber(numbers, grid, x+1, y)
            if not addNumber(numbers, grid, x, y+1):
               addNumber(numbers, grid, x-1, y+1)
               addNumber(numbers, grid, x+1, y+1)
               
            if len(numbers) == 2:
               sum += numbers[0] * numbers[1]
   
   print(filename, sum)
   return sum
      
      
assert(process("example.txt") == 467835)
assert(process("input.txt") == 84399773)
