#!/usr/bin/env python3

def process(filename):
   words = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
   sum = 0
   for line in open(filename):
      line = line.strip()
      digits = ''
      for x in range(0, len(line)):
         if line[x] >= '0' and line[x] <= '9':
            digits += line[x]
            break
         found = False
         for i in range(1, len(words)):
            if line[x:x+len(words[i])] == words[i]:
               digits += str(i)
               found = True
               break
         if found:
            break
            
      for x in range(len(line)-1, -1, -1):
         if line[x] >= '0' and line[x] <= '9':
            digits += line[x]
            break
         found = False
         for i in range(1, len(words)):
            if line[x-len(words[i])+1:x+1] == words[i]:
               digits += str(i)
               found = True
               break
         if found:
            break
   
      sum += int(digits)
   print(filename, sum)
   return sum

assert(process('example2.txt') == 281)
assert(process('input.txt') == 53312)
