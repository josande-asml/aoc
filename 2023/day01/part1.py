#!/usr/bin/env python3

def process(filename):
   sum = 0
   for line in open(filename):
      line = line.strip()
      digits = ''
      for x in range(0, len(line)):
         if line[x] >= '0' and line[x] <= '9':
            digits += line[x]
            break
      for x in range(len(line)-1, -1, -1):
         if line[x] >= '0' and line[x] <= '9':
            digits += line[x]
            break
      sum += int(digits)
   print(filename, sum)
   return sum
   
assert(process('example.txt') == 142)
assert(process('input.txt') == 53386)
