#f = open('example.txt')
f = open('input.txt')
grid = []
for line in f:
   line = line.strip()
   row = [ c for c in line ]
   grid += [ row ]
H = len(grid)
W = len(grid[0])

count = 0
dirs = [ [ 1, 0 ], [ 0, 1 ], [ 1, 1 ], [ -1, 1 ] ]
word = "XMAS"
for y in range(H):
   for x in range(W):
      for dx, dy in dirs:
         lettersFound = 0
         for i in range(len(word)):
            if y+i*dy >= 0 and y+i*dy < H and \
               x+i*dx >= 0 and x+i*dx < W and \
               grid[y+i*dy][x+i*dx] == word[i]:
               lettersFound += 1
         if lettersFound == len(word): count += 1
         
         lettersFound = 0
         for i in range(len(word)):
            if y-i*dy >= 0 and y-i*dy < H and \
               x-i*dx >= 0 and x-i*dx < W and \
               grid[y-i*dy][x-i*dx] == word[i]:
               lettersFound += 1
         if lettersFound == len(word): count += 1

print(count)  # 2493
