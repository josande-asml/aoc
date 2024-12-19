import re

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
   isCorrectFromStart = True
   while True:
      isValid = True
      for i in range(len(pages)-1):
         for j in range(i+1, len(pages)):
            for order in orderList:
               if order[1] == pages[i] and order[0] == pages[j]:
                  isCorrectFromStart = False
                  isValid = False

                  temp = pages[i]
                  pages[i] = pages[j]
                  pages[j] = temp
      if isValid: break

   if not isCorrectFromStart:
      sum += int(pages[len(pages)//2])

print(sum)  # 4681

