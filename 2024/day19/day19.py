#!/usr/bin/env python3

# Try all possible towels to match the first 'n' characters
# of the pattern. If a towel is less than 'n' characters,
# then we can prefix the other characters using the 
# combinations we found earlier for that amount of characters.
#
# For example when counting the number of combinations for
# a pattern of length 7, we try all possible towels at the
# end of it:
#
#    pattern: rwrgbwu
#    towel:        wu
#    combis:  <-5->
#
#    pattern: rwrgbwu
#    towel:      gbwu
#    combis:  <3>

def findAllCombinations(pattern, towels):
   nrcombis = [ 0 for i in range(len(pattern)+1) ]
   for n in range(1, len(pattern)+1):
      count = 0
      for towel in towels:
         if len(towel) > n: continue
         if pattern[n-len(towel):n] == towel:
            prefix = n-len(towel)
            if prefix == 0:
               count += 1
            else:
               count += nrcombis[prefix]
      nrcombis[n] = count
   return nrcombis[len(pattern)]


def process(filename):
   f = open(filename)
   towels = [ x.strip() for x in f.readline().split(',')]

   nrPossible = 0
   nrCombis = 0
   for line in f:
      pattern = line.strip()
      if len(pattern) == 0: continue
      count = findAllCombinations(pattern, towels)
      if count > 0:
         nrPossible += 1
      nrCombis += count

   print(filename, nrPossible, nrCombis)
   return (nrPossible, nrCombis)


assert(process('example.txt') == (6, 16))
assert(process('input.txt') == (272, 1041529704688380))
