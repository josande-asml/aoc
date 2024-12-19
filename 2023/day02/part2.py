#!/usr/bin/env python3

def process(filename):
   sum = 0
   for line in open(filename):
      parts = line.strip().split(": ")
      gameId = int(parts[0].split()[1])
      sets = parts[1].split(';')
      
      minRed = 0
      minGreen = 0
      minBlue = 0
      
      for s in sets:
         colors = s.strip().split(',')
         for c in colors:
            amount, col = c.split()
            amount = int(amount)
      
            if col == "red":   minRed   = max(minRed,   amount)
            if col == "green": minGreen = max(minGreen, amount)
            if col == "blue":  minBlue  = max(minBlue,  amount)
            
      sum += minRed * minGreen * minBlue
         
   print(filename, sum)
   return sum
      
assert(process('example.txt') == 2286)
assert(process('input.txt') == 78669)
