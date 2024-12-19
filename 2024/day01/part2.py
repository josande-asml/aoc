#f = open("example.txt", "r")
f = open("input.txt", "r")

a = []
b = []
for line in f:
   parts = line.split()
   a += [ int(parts[0]) ]
   b += [ int(parts[1]) ]

sum = 0
for n in a:
   count = 0
   for i in range(len(b)):
      if n == b[i]:
         count += 1
   sum += n*count
     
print(sum)  # 23741109
