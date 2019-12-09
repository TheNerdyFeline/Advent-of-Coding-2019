wire_a = ['R8','U5','L5','D3']
wire_b = ['U7','R6','D4','L4']

def grid_points(w, w_id):
	#currPoint= (x, y)
	coords = {}
	x = 0
	y = 0
	for d in w:
		dirc = d[0]
		steps = int(d[1:])
		for _ in range(0, steps):
			if dirc == 'U':
				x += 1
				currPoint = (x, y)
				coords[currPoint] = w_id
			elif dirc == 'D':
				x -= 1
				currPoint = (x, y)
				coords[currPoint] = w_id
			elif dirc == 'R':
				y += 1
				currPoint = (x, y)
				coords[currPoint] = w_id
			elif dirc == 'L':
				y -= 1
				currPoint = (x , y)
				coords[currPoint] = w_id
	print(coords)
	return coords

def cross_points(a, b):
	seen = {}
	for coord in coords:
		c = (coords.x, coords.y)
		prev_wire = seen.get(c)
		if prev_wire:
			pass
	
#find all coordinates for first wire
# find next wire, while comparing to first to find any common points
# find closest cross from start point, not 0,0
# calculate manhatten distance from sp, x + y 

grid_points(wire_a, 'a')		
