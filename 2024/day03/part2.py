import re

#f = open('example2.txt')
f = open('input.txt')

enabled = True
sum = 0
for line in f:
	parts = re.findall('(do\\(\\)|don\'t\\(\\)|mul\\(([0-9]{1,3}),([0-9]{1,3})\\))', line)
	for part in parts:
		if part[0] == 'do()':
			enabled = True
		elif part[0] == 'don\'t()':
			enabled = False
		else:	
			if enabled:
				sum += int(part[1]) * int(part[2])

print(sum)  # 77055967
