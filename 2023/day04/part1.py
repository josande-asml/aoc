#!/usr/bin/env python3
import re

def process(filename):
   sum = 0
   for line in open(filename):
      parts = re.split(r'[:|]', line.strip())
      winning = re.split(r' +', parts[1].strip())
      having = re.split(r' +', parts[2].strip())
      
      count = 0
      for nr in having:
         if nr in winning:
            count += 1
      
      points = (1 << count) // 2
      sum += points
   
   print(filename, sum)
   return sum
   

assert(process("example.txt") == 13)
assert(process("input.txt") == 22674)
