#!/usr/bin/env python3

import heapq

blocks = []
width = 0
height = 0
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


def load(filename, w, h):
   #print("Processing", filename)
   f = open(filename)

   global blocks
   blocks = []
   for line in f:
	   parts = line.strip().split(",")
	   blocks += [[int(x) for x in parts]]
   #print(blocks)
   global width, height
   width = w
   height = h


def process(time):
   global walls, width, height
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
   #print(cost[height-1][width-1])
   return cost[height-1][width-1]


def findroadblock(filename, width, height):
   load(filename, width, height)
   low = 0
   high = len(blocks)
   while high > low+1:
      time = (low+high)//2
      if time <= low: time = low+1
      if time >= high: time = high-1
      
      path = process(time)
      #print(low, time, high, path)
     
      if path == 99999: high = time
      else: low = time

   print("Roadblock:", blocks[high-1])
   return blocks[high-1]

assert(findroadblock("example.txt", 7, 7) == [6,1])
assert(findroadblock("input.txt", 71, 71) == [34,40])


