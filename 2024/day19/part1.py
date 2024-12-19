#!/usr/bin/env python3

import copy

def isPossible(pattern, towels, parts):
   if len(pattern) == 0:
      return parts 
   for towel in towels:
      if pattern.startswith(towel):
         combi = isPossible(pattern[len(towel):], towels, parts + [ towel ])
         if len(combi) > 0: return combi
   return []


def process(filename):
   f = open(filename)

   # Load all available towels
   alltowels = [ x.strip() for x in f.readline().split(',')]
   alltowels.sort(reverse=True, key=len)

   # Remove towels that can be constructed by a combinations of other towels
   towels = []
   for x in alltowels:
      subset = copy.deepcopy(alltowels)
      subset.remove(x)
      combi = isPossible(x, subset, [])
      if not combi:
         towels += [ x ]
      
   f.readline()
   count = 0
   for line in f:
      pattern = line.strip()
  
      valid = isPossible(pattern, towels, []) 
      #print(pattern, valid)
      if valid: count += 1
   print(filename, count)
   return count

assert(process('example.txt') == 6)
assert(process('input.txt') == 272)


