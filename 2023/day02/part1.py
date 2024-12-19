#!/usr/bin/env python3

def process(filename):
   sum = 0
   for line in open(filename):
      parts = line.strip().split(": ")
      gameId = int(parts[0].split()[1])
      sets = parts[1].split(';')
      isPossible = True
      for s in sets:
         colors = s.strip().split(',')
         for c in colors:
            amount, col = c.split()
            amount = int(amount)
            if col == "red"   and amount > 12: isPossible = False
            if col == "green" and amount > 13: isPossible = False
            if col == "blue"  and amount > 14: isPossible = False
      if isPossible: 
         sum += gameId
         
   print(filename, sum)
   return sum
      
assert(process('example.txt') == 8)
assert(process('input.txt') == 2283)
