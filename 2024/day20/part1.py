#!/usr/bin/env python3

def dump(grid):
   for row in grid:
      print("".join(row))
   print()


# Find fastest route without cheating
def findShortestRoute(grid, x, y):
   # Keep track of shortest route to each position
   score = []
   for r in range(len(grid)):
      row = [ 999999 for c in range(len(grid[r]))]
      score += [row]
      
   # Iteratively explore maze
   shortest = 999999
   worklist = []
   worklist.append((x, y, 0))
   while len(worklist) > 0:
      x, y, length = worklist.pop()
      if grid[y][x] == '#': continue # walking into a wall
      if score[y][x] < length: continue # already found better route
      score[y][x] = length
      
      if grid[y][x] == 'E': # reached the end position
         if length < shortest: shortest = length
         continue
      
      worklist.append((x-1, y, length+1))
      worklist.append((x, y-1, length+1))
      worklist.append((x+1, y, length+1))
      worklist.append((x, y+1, length+1))
   return shortest


def process(filename):
   # Load grid and add additional border around it, to simply
   # boundary checks
   grid = []
   for line in open(filename):
      line = '#' + line.strip() + '#'
      row = [ c for c in line ]
      grid += [ row ]
   row = [ '#' for i in range(len(grid[0])) ]
   grid = [ row ] + grid + [ row ]
   #dump(grid)
   
   # Find start position
   for y in range(len(grid)):
      for x in range(len(grid[y])):
         if grid[y][x] == 'S':
            grid[y][x] = '.'
            startX = x
            startY = y
            break

   # Calculate normal route
   baseline = findShortestRoute(grid, startX, startY)
   print("baseline:", baseline)
   
   # Try to remove walls to create cheats
   cheats = {}
   for y in range(len(grid)):
      for x in range(len(grid[y])):
         if grid[y][x] == '#':
            if (grid[y-1][x] == '.' and grid[y+1][x] == '.') or \
               (grid[y][x-1] == '.' and grid[y][x+1] == '.'):
               grid[y][x] = '.'
               saved = baseline - findShortestRoute(grid, startX, startY)
               grid[y][x] = '#'
               
               if saved in cheats:
                  cheats[saved] += 1
               else:
                  cheats[saved] = 1 

   # Count cheats
   sum = 0
   for saved in sorted(cheats.keys()):
      print(saved, cheats[saved])
      if saved >= 100:
         sum += cheats[saved]

   print(filename, sum)
   return sum


assert(process("example.txt") == 0)
assert(process("input.txt") == 1446)  # 1446 is too low
