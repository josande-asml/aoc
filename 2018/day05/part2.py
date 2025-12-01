#!/usr/bin/env python3
def react(polymer):
   hasChanged = True
   while hasChanged:
      hasChanged = False
      for i in range(len(polymer)-1):
         pair = polymer[i] + polymer[i+1]
         if polymer[i].upper() == polymer[i+1].upper() and \
            pair.upper() != pair and pair.lower() != pair:
   
   #         print(polymer[0:i] + "##" + polymer[i+2:])
            polymer = polymer[0:i] + polymer[i+2:]
   #         print(polymer)
   #         print()
            hasChanged = True
            break
   
   return len(polymer)

#f = open('example.txt')
f = open('input.txt')

polymer = f.read().strip()

bestLength = -1
for c in range(ord('a'), ord('z')+1):
   test = polymer.replace(chr(c), "").replace(chr(c).upper(), "")
   length = react(test)
   
   print(chr(c), ": ", length)

   if bestLength == -1 or length < bestLength:
      bestLength = length

print("shortest: ", bestLength)
