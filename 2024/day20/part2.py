#!/usr/bin/env python3
import time

def dump(grid):
   for row in grid:
      print("".join(row))
   print()


# Show progress
startTime = 0
def showProgress(current, total):
   global startTime
   if current == 0: 
      startTime = time.perf_counter()
   if current > 0:
      percent = 100.0*current/total
      elapsed = time.perf_counter() - startTime
      print("{0:.2f}%  ({1:.0f} seconds elapsed, {2:.0f} seconds remaining)"\
         .format(percent, elapsed, elapsed*(total-current)/current))
   

# Find fastest route with cheating
def findShortestRoute(grid, x, y, jump):
   # Keep track of shortest route to each position
   # Use 2 tables; one to see best route without cheating
   # and one for when we have already cheated
   scores = []
   for i in range(2):
      score = []
      for r in range(len(grid)):
         row = [ 999999 for c in range(len(grid[r]))]
         score += [row]
      scores += [ score ]
      
   # Iteratively explore maze
   shortest = 999999
   worklist = []
   worklist.append((x, y, 0, 0))
   while len(worklist) > 0:
      x, y, length, nrCheats = worklist.pop()
      if grid[y][x] == '#': continue # walking into a wall
      if scores[nrCheats][y][x] < length: continue # already found better route
      if nrCheats > 0 and scores[0][y][x] < length: continue # even found better route without cheating!
      scores[nrCheats][y][x] = length
      
      if grid[y][x] == 'E': # reached the end position
         if length < shortest: shortest = length
         continue
      
      worklist.append((x-1, y, length+1, nrCheats))
      worklist.append((x, y-1, length+1, nrCheats))
      worklist.append((x+1, y, length+1, nrCheats))
      worklist.append((x, y+1, length+1, nrCheats))
      
      if nrCheats == 0 and (x, y) == jump[0]:
         x, y = jump[1]
         worklist.append((x, y, length+jump[2], nrCheats+1))
   return shortest


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
            startX = x
            startY = y
            break

   # Calculate normal route
   jump = [(-1, -1), (-1, -1), 0]
   baseline = findShortestRoute(grid, startX, startY, jump)
   print("baseline:", baseline)

   # Count number of options (just to be able to show progress)
   totalOptions = 0
   for y in range(len(grid)):
      for x in range(len(grid[y])):
         if grid[y][x] != '#': totalOptions += 1
   
   # Try all possible cheats
   cheats = {}
   optionCounter = 0
   for y in range(len(grid)):
      for x in range(len(grid[y])):
         if grid[y][x] != '#':
            showProgress(optionCounter, totalOptions)
            optionCounter += 1
            for dy in range(-maxCheatLength, maxCheatLength+1):
               for dx in range(-maxCheatLength, maxCheatLength+1):
                  dist = abs(dx) + abs(dy)
                  if dist > 1 and dist <= maxCheatLength and \
                     x+dx > 0 and x+dx < len(grid[y]) and \
                     y+dy > 0 and y+dy < len(grid) and \
                     grid[y+dy][x+dx] != '#':
                        jump = [(x, y), (x+dx, y+dy), dist]
                        saved = baseline - findShortestRoute(grid, startX, startY, jump)
                        if saved > 0:
                           if saved in cheats:
                              cheats[saved] += 1
                           else:
                              cheats[saved] = 1 

   # Count cheats
   sum = 0
   for saved in sorted(cheats.keys()):
      print(saved, cheats[saved])
      if saved >= threshold:
         sum += cheats[saved]

   print(filename, sum)
   return sum


assert(process("example.txt", 2, 0) == 44)
assert(process("example.txt", 20, 50) == 285)
assert(process("input.txt", 20, 100) == 0)
