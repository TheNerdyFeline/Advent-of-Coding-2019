import sys

def create_map():
	orbits = {}
	data = []
	for line in sys.stdin:
		data.append(line.split(')'))
	for d in data:
		orb = d[1].rstrip()
		orbits[orb] = d[0]
	count_orbits(orbits)
	my_path = find_path(orbits, 'YOU')
	santas_path = find_path(orbits, 'SAN')
	hops_santa(my_path, santas_path)

def count_orbits(inp):
	oc = 0
	for o in inp:
		oc += 1
		next_orbit = inp[o]
		while next_orbit != 'COM':
			oc += 1
			next_orbit = inp[next_orbit] 
	print('p1', oc)

def find_path(inp, start):
	oc = 0
	path = []
	loc = inp[start]
	while loc != 'COM':
		path.append(loc)
		loc = inp[loc]
	return path
			
def hops_santa(my_path, santa_path):
	oc = 0
	for obj in my_path:
		if obj in santa_path:
			hops_santa_parent = santa_path.index(obj)
			hops_my_parent = my_path.index(obj)
			oc = hops_santa_parent + hops_my_parent
			break
	print('p2', oc)


create_map()
