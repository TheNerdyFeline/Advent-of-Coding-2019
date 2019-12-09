import math
wire_a = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49' , 'R71', 'U7', 'L72']
wire_b = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
coords = {}
md = []

def grid_points(w, w_id):
	x = 0
	y = 0
	def cross_point(cp):
		check_c = coords.get(cp)
		if check_c and check_c != w_id:
			cmd = abs(cp[0]) + abs(cp[1])
			md.append(cmd)
		else:
			coords[cp] = w_id
	for d in w:
		dirc = d[0]
		steps = int(d[1:])
		for _ in range(0, steps):
			if dirc == 'U':
				x += 1
				currPoint = (x, y)
				cross_point(currPoint)
			elif dirc == 'D':
				x -= 1
				currPoint = (x, y)
				cross_point(currPoint)
			elif dirc == 'R':
				y += 1
				currPoint = (x, y)
				cross_point(currPoint)
			elif dirc == 'L':
				y -= 1
				currPoint = (x , y)
				cross_point(currPoint)
	if len(md) > 0: print(min(md))
	#return coords

grid_points(wire_a, 'a')		
grid_points(wire_b, 'b')
