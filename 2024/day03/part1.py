import re

#f = open('example.txt')
f = open('input.txt')

sum = 0
for line in f:
	parts = re.findall('mul\\(([0-9]{1,3}),([0-9]{1,3})\\)', line)
	for mul in parts:
		sum += int(mul[0]) * int(mul[1])

print(sum)  # 153469856

