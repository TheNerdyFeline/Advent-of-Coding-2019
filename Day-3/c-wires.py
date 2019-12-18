import sys
import math

grid = {}
cps = {}
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
			cp = grid.get((x, y), ts)
			cts = cp + ts
			if grid.get((x, y)) and wire > 0:
				cps[(x, y)] = cts
				if cts < best:
					best = cts
			grid[(x, y)] = ts

print(best)
#293494 too high
#7961 too low
#6442 too low
