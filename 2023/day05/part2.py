#!/usr/bin/env python3
import re

# Convert ranges via mapping tables into other ranges
# Sometimes it is necessary to split a range into smaller
# sub-ranges
def convert(ranges, tables):
   for table in tables:
      remapped = []
      for mapping in table:
         map_offset = mapping[0] - mapping[1]
         map_from = mapping[1]
         map_to = mapping[1] + mapping[2]
         
         new_ranges = []
         for r in ranges:
            range_from = r[0]
            range_to = r[1]
         
            # if range does not fall in mapping, leave it unaltered
            if range_from >= map_to or \
               range_to <= map_from:
               new_ranges += [ r ]
            else:            
               # split range and apply conversion only partly
               if range_from < map_from:
                  assert(range_to > map_from)
                  new_ranges += [ [range_from, map_from] ]
                  range_from = map_from               
               
               if range_to > map_to:
                  assert(range_from < map_to)
                  new_ranges += [ [map_to, range_to] ]
                  range_to = map_to
               
               assert(range_from >= map_from)
               assert(range_to <= map_to)
               remapped += [ [range_from + map_offset, range_to + map_offset] ]
         
         ranges = new_ranges
      ranges += remapped
   return ranges


def process(filename):
   f = open(filename)
   
   # Read seed range list
   line = f.readline()
   seeds = [ int(x) for x in line.split()[1:] ]
   seedranges = []
   for i in range(len(seeds)//2):
      seedranges += [ [seeds[i*2], seeds[i*2]+seeds[i*2 + 1]] ]
   
   # Read mapping tables
   tables = []
   table = []
   for line in f:
      if len(line.split()) == 3:
         table += [[ int(x) for x in line.split() ]]
      else:
         if len(table) > 0:
            tables += [ table ]
            table = []
   if len(table) > 0:
      tables += [ table ]

   # Convert seed ranges
   locationRanges = convert(seedranges, tables)
   
   lowest = locationRanges[0][0]
   for r in locationRanges:
      if r[0] < lowest:
         lowest = r[0]

   print(filename, lowest)
   return lowest


assert(process("example.txt") == 46)
assert(process("input.txt") == 137516820)
