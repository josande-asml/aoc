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
print(react(polymer))  # 11364
