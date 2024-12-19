# Advent of Code

Solutions to the [Advent of Code](https://adventofcode.com/) puzzles. 
Beware that the goal of these program is to find the solution to a puzzle quick. This is not readable, maintainable, extensible code ;-)

Check day 7 for an interesting benchmark:

```
Performance on MacMini M2:
   C (1.14s)
      $ gcc part2.c -O3 -o part2 && time ./part2
   
   Azul Java (1.63s)
      $ javac part2.java && time java part2

   Compiled Python (2.86s)
      $ codon build part2.py && time ./part2

   Python (58.07s)
      $ time python3 part2.py
```
