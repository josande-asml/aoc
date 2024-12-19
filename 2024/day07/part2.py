#!/usr/bin/env codon run
import re

#f = open('example.txt')
f = open('input.txt')
sum = 0
for line in f:
   parts = re.split(':', line.strip())
   target = int(parts[0])
   values = [int(x) for x in parts[1].split()]

   nrCombinations = 3
   for j in range(len(values)-1):
      nrCombinations *= 3
   
   for i in range(nrCombinations):
      out = values[0]
      mask = i
      for j in range(len(values)-1):
         oper = mask % 3
         mask = mask // 3
         
         if oper == 0:
            out += values[j+1]
         elif oper == 1:
            out *= values[j+1]
         else:
            shift = 1
            while values[j+1] >= shift:
               shift = shift*10
            out = out*shift + values[j+1]
      
      if target == out:
         sum += target
         break
         
print(sum)  # 116094961956019
