import sys
import math

grid = {}
best = math.inf
moves = {'U': (+0, +1), 'D': (+0, -1), 'R': (+1, +0), 'L': (-1, +0)}

for wire, line in enumerate(sys.stdin):
	x, y = 0, 0
	ts = 0
	for move in line.split(','):
		dx, dy = moves[move[0]]
		for _ in range(int(move[1:])):
			x, y = x + dx, y + dy
			ts += 1
			#mdist = abs(x) + abs(y)
			if grid.get((x, y), wire) != wire:
				print(x, y, ts)
				best = mdist
			grid[(x, y, ts)] = wire

print(best)
