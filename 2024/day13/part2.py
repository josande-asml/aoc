#!/usr/bin/env python3

#f = open('example.txt')
f = open('input.txt')

# Solve linear equations:
#     na*adx + nb*bdx = x
#     na*ady + nb*bdy = y
#
#  nb = (x - na*adx)/bdx
#
#  na*ady + (x - na*adx)*bdy/bdx = y
#
#  na*ady*bdx/bdy + x - na*adx = y*bdx/bdy
#
#  na*(ady*bdx/bdy - adx) + x = y*bdx/bdy
#
#  na = (y*bdx/bdy - x)/(ady*bdx/bdy - adx)

def solve(adx, ady, bdx, bdy, x, y):
   #print("adx=", adx, ", ady=", ady, ", bdx=", bdx, ", bdy=", bdy, ", x=", x, ", y=", y)
   
   na = round((y*bdx/bdy - x)/(ady*bdx/bdy - adx))
   nb = round((x - na*adx)/bdx)

   if na*adx + nb*bdx == x and na*ady + nb*bdy == y:
      return na*3 + nb
      
   return 0

sum = 0
item = 0
for line in f:
   line = line.strip()
   if item == 0:
      parts = line.split()
      adx = int(parts[2][2:-1])
      ady = int(parts[3][2:])
   elif item == 1:
      parts = line.split()
      bdx = int(parts[2][2:-1])
      bdy = int(parts[3][2:])
   elif item == 2:
      parts = line.split()
      x = int(parts[1][2:-1]) + 10000000000000
      y = int(parts[2][2:]) + 10000000000000
   else:
      sum += solve(adx, ady, bdx, bdy, x, y)
   item = (item + 1) % 4
   
sum += solve(adx, ady, bdx, bdy, x, y)

print(sum)  # 82510994362072
