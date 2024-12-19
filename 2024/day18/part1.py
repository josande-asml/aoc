#!/usr/bin/env python3

import heapq

blocks = []
walls = []
cost = []

def dumpwalls(time):
   for row in walls:
      for col in row:
         if col <= time:
            print("#", end="")
         else:
            print(".", end="")
      print()
   print()


def dumpcost():
   for row in cost:
      for col in row:
         if col == 99999:
            print("  . ", end="")
         else:
            print("{0:3d} ".format(col), end="")
      print()
   print()


def process(filename, width, height, time):
   print("Processing", filename)
   f = open(filename)

   global blocks
   blocks = []
   for line in f:
	   parts = line.strip().split(",")
	   blocks += [[int(x) for x in parts]]
   #print(blocks)

   global walls
   walls = []
   for y in range(height):
      row = []
      for x in range(width):
         row += [ 99999 ]
      walls += [ row ]

   for n in range(len(blocks)):
      x, y = blocks[n]
      walls[y][x] = n+1
   #dumpwalls(time)

   global cost
   cost = []
   for y in range(height):
      row = []
      for x in range(width):
         row += [ 99999 ]
      cost += [ row ]

   worklist = []
   heapq.heapify(worklist)
   heapq.heappush(worklist, (0, 0, 0))
   while len(worklist) > 0:
      x, y, step = worklist.pop()

      # valid position?
      if x < 0 or x >= width or y < 0 or y >= height: continue
      #if walls[y][x] < step: continue   # part2?
      if walls[y][x] <= time: continue 

      # better route to this position?
      if cost[y][x] <= step: continue
      cost[y][x] = step
      
      # reached the exit?
      if x == width-1 and y == height-1: continue

      # plan next step
      heapq.heappush(worklist, (x-1, y, step+1))
      heapq.heappush(worklist, (x, y-1, step+1))
      heapq.heappush(worklist, (x+1, y, step+1))
      heapq.heappush(worklist, (x, y+1, step+1))

   #dumpcost()
   print(cost[height-1][width-1])
   return cost[height-1][width-1]

assert(process("example.txt", 7, 7, 12) == 22)
assert(process("input.txt", 71, 71, 1024) == 320)

