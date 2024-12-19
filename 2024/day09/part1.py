#!/usr/bin/python3

def dump(disk):
   image = ""
   for i in range(len(disk)):
      if disk[i] == -1:
         image += "."
      else:
         image += str(disk[i])
   print(image)


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
   for j in range(n):
      disk += [ id ]
   id += 1

   if i < len(line):
      n = int(line[i])
      i += 1
      for j in range(n):
         disk += [ -1 ]

# Compact disk
left = 0
right = len(disk)-1

while True:
   while disk[left] != -1 and left+1 < len(disk):
      left += 1
   while disk[right] == -1 and right-1 >= 0:
      right -= 1
   if left >= right: break

   disk[left] = disk[right]
   disk[right] = -1

# Calculate checksum
chksum = 0
for i in range(len(disk)):
   if disk[i] != -1:
      chksum += i*disk[i]
print(chksum)  # 6242766523059

#dump(disk)
