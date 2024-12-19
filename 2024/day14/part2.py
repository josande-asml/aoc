#!/usr/bin/env python3

import re

# f = open('example.txt')
# W = 11
# H = 7

f = open('input.txt')
W = 101
H = 103

# Load lines like: "123: 234 345 456 567 678"
robots = []
for line in f:
   line = line.strip()
   parts = line.split()
   pos = [ int(x) for x in parts[0][2:].split(",") ]
   vel = [ int(x) for x in parts[1][2:].split(",") ]
   robots += [ pos + vel ]

# See if there is overlap
def hasOverlap(seconds):
   grid = []
   for y in range(H):
      row = []
      for x in range(W):
         row += [ 0 ]
      grid += [ row ]

   for robot in robots:
      x = (robot[0] + seconds*robot[2]) % W
      y = (robot[1] + seconds*robot[3]) % H
      grid[y][x] += 1
      if grid[y][x] > 1: return True

   return False

# Render image
def dump(seconds):
   print("After", seconds, "seconds:")
   grid = []
   for y in range(H):
      row = []
      for x in range(W):
         row += [ 0 ]
      grid += [ row ]

   for robot in robots:
      x = (robot[0] + seconds*robot[2]) % W
      y = (robot[1] + seconds*robot[3]) % H
      grid[y][x] += 1

   for y in range(H):
      row = ""
      for x in range(W):
         if grid[y][x] == 0:
            print(".", end="")
         else:
            print(grid[y][x], end="")
      print()
      
# Draw grid
for s in range(1, 10000):
   if not hasOverlap(s):
      dump(s)
      input()   
      