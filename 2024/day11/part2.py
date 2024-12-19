#!/usr/bin/env python3

#f = open('example.txt')
f = open('input.txt')

# Load lines like: "123: 234 345 456 567 678"
stones = {}
for line in f:
   line = line.strip()
   for x in line.split():
      value = int(x)
      if value in stones:
         stones[value] += 1
      else:
         stones[value] = 1

for n in range(75):
   new = {}
   for stone, freq in stones.items():
      digits = str(stone)
      if stone == 0:
         if 1 in new:
            new[1] += freq
         else:
            new[1] = freq
      elif len(digits) % 2 == 0:
         left = int(digits[0:len(digits)//2])
         right = int(digits[len(digits)//2:])
         if left in new:
            new[left] += freq
         else:
            new[left] = freq
         if right in new:
            new[right] += freq
         else:
            new[right] = freq
      else:
         value = stone*2024
         if value in new:
            new[value] += freq
         else:
            new[value] = freq
   stones = new
   
count = 0
for freq in stones.values():
   count += freq
print(count)  # 257246536026785
