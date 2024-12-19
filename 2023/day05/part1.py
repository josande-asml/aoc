#!/usr/bin/env python3
import re

def process(filename):
   f = open(filename)
   
   # Read seed list
   line = f.readline()
   seeds = [ int(x) for x in line.split()[1:] ]
   
   # Read mapping tables
   tables = []
   mapping = []
   for line in f:
      if len(line.split()) == 3:
         mapping += [[ int(x) for x in line.split() ]]
      else:
         if len(mapping) > 0:
            tables += [ mapping ]
            mapping = []
   if len(mapping) > 0:
      tables += [ mapping ]

   # Convert seeds
   lowest = -1
   for id in seeds:
      for mapping in tables:
         for rule in mapping:
            if id >= rule[1] and id < rule[1]+rule[2]:
               id += rule[0] - rule[1]
               break
      if lowest == -1 or id < lowest: 
         lowest = id
   
   print(filename, lowest)
   return lowest


assert(process("example.txt") == 35)
assert(process("input.txt") == 389056265)
