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

def count_orbits(inp):
	oc = 0
	for o in inp:
		oc += 1
		next_orbit = inp[o]
		while next_orbit != 'COM':
			oc += 1
			next_orbit = inp[next_orbit]
	print(oc)

create_map()
