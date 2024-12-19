#!/usr/bin/env python3

import copy

# Try all possible towels to match the first 'l' characters
# of the pattern. Prepend the towel with a base pattern to
# come to the exact length. Keep track of the number of ways
# to match a certain pattern length

def findAllCombinations(pattern, towels):
   nrcombis = [ 0 for i in range(len(pattern)+1) ]
   for l in range(1, len(pattern)+1):
      count = 0
      for towel in towels:
         if len(towel) > l: continue
         if pattern[l-len(towel):l] == towel:
            base = l-len(towel)
            if base == 0:
               count += 1
            else:
               count += nrcombis[base]
      nrcombis[l] = count

   #print(pattern, nrcombis[len(pattern)], nrcombis)
   return nrcombis[len(pattern)]


def process(filename):
   f = open(filename)

   # Load all available towels
   towels = [ x.strip() for x in f.readline().split(',')]

   # Try to make all patterns      
   f.readline()
   nrPossible = 0
   nrCombis = 0
   for line in f:
      pattern = line.strip()
      count = findAllCombinations(pattern, towels)
      if count > 0:
         nrPossible += 1
      nrCombis += count

   print(filename, nrPossible, nrCombis)
   return (nrPossible, nrCombis)

assert(process('example.txt') == (6, 16))
assert(process('input.txt') == (272, 1041529704688380))

