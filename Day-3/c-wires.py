import sys
import math

grid = {}
best = math.inf
moves = {'U': (+0, +1), 'D': (+0, -1), 'R': (+1, +0), 'L': (-1, +0)}

for wire, line in enumerate(sys.stdin):
	x, y = 0, 0
	ts = 0
	#print(wire)
	for move in line.split(','):
		dx, dy = moves[move[0]]
		for _ in range(int(move[1:])):
			x, y = x + dx, y + dy
			ts += 1
			#mdist = abs(x) + abs(y)
			cp = grid.get((x, y), ts)
			cts = cp + ts
			if grid.get((x, y)) and wire > 0:
				best = cts
				print(ts, grid.get(x, y), cp, best)
			grid[(x, y)] = ts + wire

print(best) 
#293494 too high
#7961 too low
#6442 too low
