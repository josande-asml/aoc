#f = open("example.txt", "r")
f = open("input.txt", "r")

a = []
b = []
for line in f:
   parts = line.split()
   a += [ int(parts[0]) ]
   b += [ int(parts[1]) ]

a.sort()
b.sort()

sum = 0
for i in range(len(a)):
   diff = abs(a[i] - b[i])
   sum += diff

print(sum)  # 2166959
