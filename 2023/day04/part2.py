#!/usr/bin/env python3
import re

def process(filename):
   lines = open(filename).readlines()
   counts = [ 1 for i in range(0, len(lines)) ]
   
   for i in range(0, len(lines)):
      line = lines[i].strip()
      parts = re.split(r'[:|]', line)   
      winning = re.split(r' +', parts[1].strip())
      having = re.split(r' +', parts[2].strip())
      
      matches = 0
      for nr in having:
         if nr in winning:
            matches += 1
   
      for j in range(i+1, i+matches+1):
         counts[j] += counts[i]
   
   sum = 0
   for i in range(0, len(counts)):
      sum += counts[i]

   print(filename, sum)
   return sum
   

assert(process("example.txt") == 30)
assert(process("input.txt") == 5747443)
