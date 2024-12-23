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
   
   # Find islands of mutually directly connected systems
   islands = []
   for a in directconns.keys():
      found = False
      for island in islands:
         if a in island:
            found = True
      if found: continue
      island = [ a ]

      for b in directconns[a]:   # try to add 'b' to island
         isFullyConnected = True
         for i in island:
            if i not in directconns[b]:
               isFullyConnected = False
         if isFullyConnected:
            island += [b]
      
      islands += [island]

   # Find largest island
   largest = islands[0]
   for island in islands:
      if len(island) > len(largest):
         largest = island

   password = ','.join(sorted(largest))
   print(filename, password)
   return password


assert(process("example.txt") == "co,de,ka,ta")
assert(process("input.txt") == "cl,df,ft,ir,iy,ny,qp,rb,sh,sl,sw,wm,wy")
