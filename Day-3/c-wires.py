import sys
import math

grid = {}
cps = {}
best = math.inf
moves = {'U': (+0, +1), 'D': (+0, -1), 'R': (+1, +0), 'L': (-1, +0)}
wire_a = sys.stdin.readline().split(',')
wire_b = sys.stdin.readline().split(',')

def calc_points_steps(path):
	points = {}
	ts = 0
	x, y = 0, 0
	for move in (path):
		dx, dy = moves[move[0]]
		for _ in range(int(move[1:])):
			x, y = x + dx, y + dy
			ts += 1
			if (x, y) not in points:
				points[(x, y)] = ts
	return points

a_points = calc_points_steps(wire_a)
b_points = calc_points_steps(wire_b)
inter_points = [point for point in a_points if point in b_points]

p2 = min(a_points[point] + b_points[point] for point in inter_points)
print(p2)

#293494 too high
#7961 too low
#6442 too low
