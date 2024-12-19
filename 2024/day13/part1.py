#!/usr/bin/env python3

#f = open('example.txt')
f = open('input.txt')

def solve(adx, ady, bdx, bdy, x, y):
   #print("adx=", adx, ", ady=", ady, ", bdx=", bdx, ", bdy=", bdy, ", x=", x, ", y=", y)
   besttokens = 0
   for na in range(100):
      if bdx > 0:
         nb = (x - na*adx) // bdx   
      else:
         nb = (y - na*ady) // bdy   
      if nb < 0: continue
      tokens = na*3 + nb
      
      if na*adx + nb*bdx == x and na*ady + nb*bdy == y:
         #print("na=", na, ", nb=", nb, ", x=", na*adx + nb*bdx, ", y=", na*ady + nb*bdy, ", tokens=", tokens)
         
         if besttokens == 0 or tokens < besttokens:
            besttokens = tokens
   return besttokens

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
      x = int(parts[1][2:-1])
      y = int(parts[2][2:])
   else:
      sum += solve(adx, ady, bdx, bdy, x, y)
   item = (item + 1) % 4
   
sum += solve(adx, ady, bdx, bdy, x, y)

print(sum)  # 35997
