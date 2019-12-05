wire_a = ['R8','U5','L5','D3']
wire_b = ['U7','R6','D4','L4']

def grid_points(w):
	coord = []
	currPoint= [0, 0]
	x = currPoint[0]
	y = currPoint[1]
	print(x, y)
	for d in w:
		dirc = d[0]
		steps = int(d[1])
		if dirc == 'U':
			c = 1
			while c < steps:
				currPoint = [x, y += 1]
				coord.append(currPoint)
				c += 1
		elif dirc == 'D':
			c = steps
			while c > 0:
				currPoint = [x, y -= 1]
				coord.append(currPoint)
				c -= 1
		elif dirc == 'R':
			c = 1
			while c < steps:
				currPoint = [x += 1, y]
				coord.append(currPoint)
				c += 1
		elif dirc == 'L':
			c = steps
			while c > 0:
				currPoint = [x -= 1, y]
				coord.append(currPoint)
				c -= 1
	print(coord)

def cross_points(a, b):
	aCoord = []
	bCoord = []

#find all coordinates for each wire
# compare to find any common points
# find closest cross from start point, not 0,0
# calculate manhatten distance from sp, x + y 

grid_points(wire_a)		
