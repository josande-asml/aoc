#!/usr/bin/env python3

# Return the value of card (2 .. 14)
def cardValue(card):
	return 2 + "23456789TJQKA".index(card)
	

def handValue(hand):
	sorted(hand)
	
	# Value of individual cards
	value = \
	   100000000*cardValue(hand[0]) + \
		1000000*cardValue(hand[1]) + \
		10000*cardValue(hand[2]) + \
		100*cardValue(hand[3]) + \
		cardValue(hand[4])
	
	# Count card freq
	freq = [ 0 for c in range(0, 15) ]
	for card in hand:
		freq[cardValue(card)] += 1
	freq = sorted(freq, reverse=True)
	
	# Five of a kind
	if freq[0] == 5: return 60000000000 + value
	
	# Four of a kind
	if freq[0] == 4: return 50000000000 + value
	
	# Full house
	if freq[0] == 3 and freq[1] == 2: return 40000000000 + value

	# Three of a kind
	if freq[0] == 3: return 30000000000 + value

	# Two pair
	if freq[0] == 2 and freq[1] == 2: return 20000000000 + value

	# One pair
	if freq[0] == 2: return 10000000000 + value

	# High card
	return value


def process(filename):
	hands = {}
	for line in open(filename):
		hand, bid = line.strip().split()
		hands[handValue(hand)] = (hand, int(bid))
		
	order = sorted(hands)
	winnings = 0
	rank = 1
	for o in order:
		print(rank, hands[o][0], o, hands[o][1])
		winnings += rank * hands[o][1]
		rank += 1
	
	print(filename, winnings)
	return winnings


assert(process("example.txt") == 6440)
assert(process("input.txt") == 250957639)
                               
