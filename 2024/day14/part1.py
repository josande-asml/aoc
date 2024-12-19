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

# Calculate in what quadrant the robots are
quadrants = [ 0, 0, 0, 0 ]
seconds = 100
for robot in robots:
   x = (robot[0] + seconds*robot[2]) % W
   y = (robot[1] + seconds*robot[3]) % H
   if x < W//2 and y < H//2: quadrants[0] += 1
   if x > W//2 and y < H//2: quadrants[1] += 1
   if x < W//2 and y > H//2: quadrants[2] += 1
   if x > W//2 and y > H//2: quadrants[3] += 1

# Calculate sum
print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])
