#!/usr/bin/env codon run

import sys

def dump(disk):
   image = ""
   for x in disk:
      sep = "|"
      for i in range(x[1]):
         if x[0] == -1:
            image += sep + "."
         else:
            image += sep + str(x[0])
         sep = " "      
   image += "|"
   print(image)


def verify(disk):
   for i in range(1, len(disk)):
      if disk[i][1] < 1:
         print("Invalid! size [", i, "]=", disk[i][1])
         sys.exit()
      if disk[i-1][0] == disk[i][0]:
         print("Invalid! [", i-1, "]=", disk[i-1][0], " and [", i, "]=", disk[i][0])
         sys.exit()


#f = open('example.txt')
f = open('input.txt')

for line in f:
   line = line.strip()

disk = []
id = 0
i = 0
while i < len(line):
   n = int(line[i])
   i += 1
   disk += [[ id, n ]]
   id += 1

   if i < len(line):
      n = int(line[i])
      i += 1
      if n > 0:
         disk += [[ -1, n ]]

# Compact disk
id = len(disk)
block = len(disk)
while block > 0:
   #dump(disk)
   #verify(disk)

   block -= 1
   while block > 0 and disk[block][0] == -1:
      block -= 1

   if disk[block][0] > id: 
      continue
   id = disk[block][0]

   gap = 0
   while gap < block and disk[gap][0] != -1 or disk[gap][1] < disk[block][1]:
      gap += 1

   if gap < block:
      if disk[gap][1] == disk[block][1]:
         # exact fit. Copy block into gap
         disk[gap][0] = disk[block][0]
      else:
         # gap is bigger. Copy block into gap and insert new smaller gap
         n = disk[gap][1]
         disk[gap][0] = disk[block][0]
         disk[gap][1] = disk[block][1]
         disk.insert(gap+1, [ -1, n-disk[gap][1] ])
         block += 1

      # remove original block and merge adjacent gaps
      disk[block][0] = -1
      while block+1 < len(disk) and disk[block+1][0] == -1:
         disk[block][1] += disk[block+1][1]
         disk = disk[0:block+1] + disk[block+2:]
      
      while block-1 >= 0 and disk[block-1][0] == -1:
         disk[block-1][1] += disk[block][1]
         disk = disk[0:block] + disk[block+1:]
         block -= 1

# Calculate checksum
chksum = 0
n = 0
for x in disk:
   for j in range(x[1]):
      if x[0] != -1:
         chksum += n*x[0]
      n += 1
print(chksum)   # 6272188244509
