#f = open("example.txt", "r")
f = open("input.txt", "r")

def isSafe(n):
   if n[1] > n[0]:
      for i in range(len(n)-1):
         if n[i+1] <= n[i] or n[i+1] > n[i]+3:
            return False
   elif n[1] < n[0]:
      for i in range(len(n)-1):
         if n[i+1] >= n[i] or n[i+1] < n[i]-3:
            return False
   else:
      return False      
   return True

count = 0
for line in f:
   parts = line.split()
   n = [ int(x) for x in parts ]
   if isSafe(n):
      count += 1

print(count)  # 356
