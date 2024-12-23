#!/usr/bin/env python3

def process(filename):
   # Read list of host names and connections
   directconns = {}
   for line in open(filename):
      a, b = line.strip().split("-")
      if a not in directconns:
         directconns[a] = [b]
      else:
         directconns[a] += [b]
         
      if b not in directconns:
         directconns[b] = [a]
      else:
         directconns[b] += [a]
   
   # Find triplets
   triplets = []
   for a in directconns.keys():
      for b in directconns[a]:
         if b <= a: continue
         for c in directconns[a]:
            if c <= b: continue
            if c in directconns[b]:
               triplet = sorted([a, b, c])
               triplets += [triplet]
   
   # Count triplets with host names starting with 't'
   count = 0
   for triplet in sorted(triplets):
      a, b, c = triplet
      if a.startswith('t') or b.startswith('t') or c.startswith('t'):
         print(a, b, c)
         count += 1
   
   print(filename, count)
   return count


assert(process("example.txt") == 7)
assert(process("input.txt") == 1227)
