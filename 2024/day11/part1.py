#!/usr/bin/env python3

#f = open('example.txt')
f = open('input.txt')

# Load lines like: "123: 234 345 456 567 678"
for line in f:
   line = line.strip()
   stones = [ int(x) for x in line.split()]

for n in range(25):
   new = []
   for stone in stones:
      digits = str(stone)
      if stone == 0:
         new += [ 1 ]
      elif len(digits) % 2 == 0:
         left = digits[0:len(digits)//2]
         right = digits[len(digits)//2:]
         new += [ int(left) ]
         new += [ int(right) ]
      else:
         new += [ stone*2024 ]
   stones = new
   
print(len(stones))  # 217443
