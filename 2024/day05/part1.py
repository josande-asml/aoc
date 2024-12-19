#f = open('example.txt')
f = open('input.txt')

orderList = []
for line in f:
   line = line.strip()
   if line == "": break
   orderList += [ line.split("|") ]

pagesList = []
for line in f:
   line = line.strip()
   if line == "": break
   pagesList += [ line.split(",") ]

sum = 0
for pages in pagesList:
   isValid = True
   for i in range(len(pages)-1):
      for j in range(i+1, len(pages)):
         for order in orderList:
            if order[1] == pages[i] and order[0] == pages[j]: isValid = False
   if isValid:
      sum += int(pages[len(pages)//2])

print(sum)  # 5091

