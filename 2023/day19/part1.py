#!/usr/bin/env python3
import re

def check(workflows, ratings):
   w = 'in'
   while w != 'A' and w != 'R':
      rules = workflows[w]
      for rule in rules:
         prop, oper, value, action = rule
         if oper == False or \
            (oper == '<' and ratings[prop] < value) or \
            (oper == '>' and ratings[prop] > value):
            w = action
            break
   return w


def process(filename):
   f = open(filename)
   
   # Read rules
   workflows = {}
   for line in f:
      line = line.strip()
      if len(line) == 0: break
      
      name, instructions = line.split('{')
      parts = instructions[:-1].split(',')
      rules = []
      for part in parts:
         eq_parts = part.split(':')
         if len(eq_parts) == 1:
            action = eq_parts[0]
            prop = oper = value = False
            oper = False
            value = False
         else:
            action = eq_parts[1]
            prop = eq_parts[0][0]
            if prop == 'x': prop = 0
            if prop == 'm': prop = 1
            if prop == 'a': prop = 2
            if prop == 's': prop = 3
            oper = eq_parts[0][1]
            value = int(eq_parts[0][2:])
         rules += [ (prop, oper, value, action) ]
      workflows[name] = rules
   
   # Read ratings
   sum = 0
   for line in f:
      match = re.findall('[xmas]=(\\d+)', line)
      ratings = [int(x) for x in match]

      if check(workflows, ratings) == 'A':
         sum += ratings[0] + ratings[1] + ratings[2] + ratings[3]

   print(filename, sum)   
   return sum

assert(process("example.txt") == 19114)
assert(process("input.txt") == 342650)
