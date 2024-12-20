#!/usr/bin/env python3
import time

def dump(grid):
   for row in grid:
      print("".join(row))
   print()


# For all positions on the grid calculate fastest route 
# to end position without cheating
def findShortestRoute(grid):
   # Find end position
   for y in range(len(grid)):
      for x in range(len(grid[y])):
         if grid[y][x] == 'E':
            endX, endY = x, y
            break

   # Keep track of shortest route to each position
   distance = []
   for r in range(len(grid)):
      row = [ 999999 for c in range(len(grid[r]))]
      distance += [row]
      
   # Iteratively explore maze
   shortest = 999999
   worklist = []
   worklist.append((endX, endY, 0))
   while len(worklist) > 0:
      x, y, length = worklist.pop()
      if grid[y][x] == '#': continue # walking into a wall
      if distance[y][x] < length: continue # already found better route
      distance[y][x] = length
      if grid[y][x] == 'S': continue # reached the start position
      
      worklist.append((x-1, y, length+1))
      worklist.append((x, y-1, length+1))
      worklist.append((x+1, y, length+1))
      worklist.append((x, y+1, length+1))
   return distance


def process(filename, maxCheatLength, threshold):
   # Load grid and add additional border around it, to simplify
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
            startX, startY = x, y
            break

   # Calculate distance from each position to end
   distance = findShortestRoute(grid)
   
   # Try all possible cheats
   cheats = {}
   for y in range(len(grid)):
      for x in range(len(grid[y])):
         if grid[y][x] != '#':
            for dy in range(-maxCheatLength, maxCheatLength+1):
               for dx in range(-maxCheatLength, maxCheatLength+1):
                  dist = abs(dx) + abs(dy)
                  if dist > 1 and dist <= maxCheatLength and \
                     x+dx > 0 and x+dx < len(grid[y]) and \
                     y+dy > 0 and y+dy < len(grid) and \
                     grid[y+dy][x+dx] != '#':
                     
                     saving = distance[y][x] - (distance[y+dy][x+dx] + dist)
                     if saving > 0:
                        if saving in cheats:
                           cheats[saving] += 1
                        else:
                           cheats[saving] = 1 

   # Count cheats
   sum = 0
   for saving in sorted(cheats.keys()):
      print(saving, cheats[saving])
      if saving >= threshold:
         sum += cheats[saving]

   print(filename, sum)
   return sum


assert(process("example.txt", 2, 0) == 44)
assert(process("example.txt", 20, 50) == 285)
assert(process("input.txt", 20, 100) == 1017615)
