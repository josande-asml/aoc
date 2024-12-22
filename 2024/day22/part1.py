#!/usr/bin/env python3

def next(number):
	number = (number ^ (number << 6)) & 0xffffff
	number = (number ^ (number >> 5)) & 0xffffff
	number = (number ^ (number << 11)) & 0xffffff
	return number

def process(filename):
	sum = 0
	for line in open(filename):
		number = int(line.strip())
		for i in range(2000):
			number = next(number)
		sum += number
		
	print(filename, sum)		
	return sum
	
assert(process("example.txt") == 37327623)
assert(process("input.txt") == 14273043166)
