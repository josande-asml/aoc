#!/usr/bin/env python3

def dump():
   global A, B, C, program, IP, out

   print("Register A:", A)
   print("Register B:", B)
   print("Register C:", C)
   print("Program:", program)
   print("IP:", IP)
   print("Out: \"", out, "\"", sep="")
   print()


def load(filename):
   global A, B, C, program, IP, out

   print("Processing", filename)
   f = open(filename)
   A = int(f.readline().split()[2])
   B = int(f.readline().split()[2])
   C = int(f.readline().split()[2])
   f.readline()
   program = [ int(x) for x in f.readline().split()[1].split(",") ]
   IP = 0
   out = ""


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
         if len(out) > 0: out += ","
         out += str(combo & 7)
      elif opcode == 6: # bdv (B = A // 2^combo-oper)
         B = A // (1 << combo)
      elif opcode == 7: # cdv (C = A // 2^combo-oper)
         C = A // (1 << combo)
      else: assert(False)

   #print("End State:")
   #dump()

load("example1.txt")
run()
assert(B == 1)

load("example2.txt")
run()
assert(out == "0,1,2")

load("example3.txt")
run()
assert(A == 0)
assert(out == "4,2,5,6,7,7,7,7,3,1,0")

load("example4.txt")
run()
assert(B == 26)

load("example5.txt")
run()
assert(B == 44354)

load("input.txt")
run()
assert(out == "3,4,3,1,7,6,5,6,0")

