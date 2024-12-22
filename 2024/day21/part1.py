#!/usr/bin/env python3

# Key locations
numpad = {
	'7': (0, 0),
	'8': (1, 0),
	'9': (2, 0),
	'4': (0, 1),
	'5': (1, 1),
	'6': (2 ,1),
	'1': (0, 2),
	'2': (1, 2),
	'3': (2, 2),
	'0': (1, 3),
	'A': (2, 3),
	'X': (0, 3)
}

dirpad = {
	'^': (1, 0),
	'A': (2, 0),
	'<': (0, 1),
	'v': (1, 1),
	'>': (2, 1),
	'X': (0, 0)
}


# Generate steps needed to move from `src` to `dest`
# assumption, switching direction of movement costs time,
# so movement on numeric keyboard should be an angle, not
# a zigzag. This leaves only two options per move
def generateStep(src, dest, keypad):
	moves = []
	x, y = keypad[src]
	dx = keypad[dest][0] - keypad[src][0]
	dy = keypad[dest][1] - keypad[src][1]

	if (x + dx, y) != keypad['X']:
		seq = ""
		if dx > 0:
			seq = '>'*dx
		elif dx < 0:
			seq = '<'*-dx
		if dy > 0:
			seq += 'v'*dy
		elif dy < 0:
			seq += '^'*-dy
		moves += [ seq + 'A' ]

	if dx != 0 and dy != 0 and (x, y+dy) != keypad['X']:
		seq = ""
		if dy > 0:
			seq = 'v'*dy
		elif dy < 0:
			seq = '^'*-dy
		if dx > 0:
			seq += '>'*dx
		elif dx < 0:
			seq += '<'*-dx
		moves += [ seq + 'A' ]

	return moves


def generateNumMoves(code):
	moves = []
	code = 'A' + code	 	# start at 'A'
	for i in range(len(code)-1):
		stepMoves = generateStep(code[i], code[i+1], numpad)
		newMoves = []
		if len(moves) == 0:
			newMoves = stepMoves
		else:
			for m in moves:
				for sm in stepMoves:
					newMoves += [ m + sm ]
		moves = newMoves
	return moves


def generateDirSeq(code):
	seq = ""
	code = 'A' + code	 	# start at 'A'
	for i in range(len(code)-1):
		stepMoves = generateStep(code[i], code[i+1], dirpad)
		seq += stepMoves[0]
	return seq


def findShortestSeq(code):
	seqs = []
	for move in generateNumMoves(code):
		seq = generateDirSeq(move)
		seq = generateDirSeq(seq)
		seqs += [ seq ]
	
	shortest = seqs[0]
	for seq in seqs:
		if len(seq) < len(shortest):
			shortest = seq
	
	return shortest
	

def process(filename):
   sum = 0
   for line in open(filename):
   	code = line.strip()
   	seq = findShortestSeq(code)
   	number = int(code[:-1])
   	sum += len(seq) * number

   print(filename, sum)
   return sum


assert(process("example.txt") == 126384)
assert(process("input.txt") == 203734)
