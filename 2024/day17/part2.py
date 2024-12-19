#!/usr/bin/env python3
import copy
import random

def dump():
   global A, B, C, program, IP, out

   print("Register A:", A)
   print("Register B:", B)
   print("Register C:", C)
   print("Program:", program)
   print("IP:", IP)
   print("Out:", out)
   print()


def load(filename):
   global A, B, C, program, IP, out

   f = open(filename)
   A = int(f.readline().split()[2])
   B = int(f.readline().split()[2])
   C = int(f.readline().split()[2])
   f.readline()
   program = [ int(x) for x in f.readline().split()[1].split(",") ]
   IP = 0
   out = []


def disasm():
   for i in range(0, len(program), 2):
      opcode = program[i]
      oper = program[i+1]

      print("{0:2d}: ".format(i), end="")
      if opcode == 0:
         print("adv ", "0123ABC"[oper], sep="", end="")
         print("    A /= 1<<", "0123ABC"[oper], sep="")
      elif opcode == 1:
         print("bxl ", oper, sep="", end="")
         print("    B ^= ", oper, sep="")
      elif opcode == 2:
         print("bst ", "0123ABC"[oper], sep="", end="")
         if oper < 4:
            print("    B = ", oper, sep="")
         else:
            print("    B = ", "0123ABC"[oper], " & 7", sep="")
      elif opcode == 3:
         print("jnz ", oper, sep="", end="")
         print("    if A > 0 jump to ", oper, sep="")
      elif opcode == 4:
         print("bxc", sep="", end="")
         print("      B = B^C")
      elif opcode == 5:
         print("out ", "0123ABC"[oper], sep="", end="")
         if oper < 4:
            print("    print \"", "0123ABC"[oper], "\"", sep="")
         else:
            print("    print ", "0123ABC"[oper], " & 7", sep="")
      elif opcode == 6:
         print("bdv ", "0123ABC"[oper], sep="", end="")
         print("    B = A / 1<<", "0123ABC"[oper], sep="")
      elif opcode == 7:
         print("cdv ", "0123ABC"[oper], sep="", end="")
         print("    C = A / 1<<", "0123ABC"[oper], sep="")


def run():
   global A, B, C, program, IP, out

   #print("Initial State:")
   #dump()

   while IP >= 0 and IP < len(program):
      opcode = program[IP]
      literal = program[IP+1]
      combo = program[IP+1]
      IP += 2      

      if combo < 4: pass
      elif combo == 4: combo = A
      elif combo == 5: combo = B
      elif combo == 6: combo = C

      if opcode == 0: # adv (A = A // 2^combo-oper)
         A = A // (1 << combo)
      elif opcode == 1: # blx (B = B ^ literal-oper)
         B = B ^ literal
      elif opcode == 2: # bst (B = combo-oper % 7)
         B = combo & 7
      elif opcode == 3: # jnz (A=0: nop, A > 0: IP=A)
         if A > 0: IP = literal
      elif opcode == 4: # bxc (B = B^C, oper not used)
         B = B^C
      elif opcode == 5: # out (print: combo-oper % 7)
         out += [ combo & 7 ]
      elif opcode == 6: # bdv (B = A // 2^combo-oper)
         B = A // (1 << combo)
      elif opcode == 7: # cdv (C = A // 2^combo-oper)
         C = A // (1 << combo)
      else: assert(False)

   #print("End State:")
   #dump()


def save():
   global A, B, C, program, IP, out
   global savedA, savedB, savedC, savedProgram

   savedA = A
   savedB = B
   savedC = C
   savedProgram = program


def restore():
   global A, B, C, program, IP, out
   global savedA, savedB, savedC, savedProgram

   A = savedA
   B = savedB
   C = savedC
   program = savedProgram
   IP = 0
   out = []


def calcA(value):
   A = 0
   for i in value:
      A = (A*8) + i
   return A


def calcdiff(value):
   global A, B, C, program, out, IP
   restore()
   A = calcA(value)
   run()
   while len(out) < 16: out = [ 0 ] + out
   
   target = [2,4,1,5,7,5,4,5,0,3,1,6,5,5,3,0]
   diff = 0
   for i in range(len(target)):
      diff += abs(target[i] - out[i])
   return diff


load("example6.txt")
A = 117440
run()
assert(out == [0,3,5,4,3,0])

load("input.txt")
save()
A = 109019930331546 # value = [3, 0, 6, 2, 3, 4, 5, 6, 1, 6, 1, 0, 4, 6, 3, 2] 
run()
assert(out == [2,4,1,5,7,5,4,5,0,3,1,6,5,5,3,0])

restore()
A = 136902858044169 # value = [3, 7, 1, 0, 1, 4, 5, 6, 1, 6, 1, 7, 1, 4, 1, 1]
run()
assert(out == [2,4,1,5,7,5,4,5,0,3,1,6,5,5,3,0])
 
#dump()
#disasm()

while True:
   # choose random start value
   print()
   value = [ random.randint(0, 7) for i in range(16) ]
   diff = calcdiff(value)
   while True:
      # try all possible single-digit mutations to see what works best
      bestdiff = -1
      for i in range(16):
         temp = value[i]
         for j in range(8):
            value[i] = j
            d = calcdiff(value)
            if bestdiff == -1 or d < bestdiff:
               bestvalue = copy.deepcopy(value)
               bestdiff = d
         value[i] = temp

      if bestdiff < diff:
         maxIter = 0
         value = bestvalue
         diff = bestdiff
         calcdiff(value)
         print(value, "{0:2d}".format(diff), out)
         if diff == 0:
            print("FOUND! A=",calcA(value))
            exit()
      else:
         break

