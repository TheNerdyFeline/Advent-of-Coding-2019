from numpy import loadtxt
from copy import copy

data = loadtxt('data.txt', comments='#', dtype='int', delimiter=',', unpack=False)
address = 19690720

def add(x, y):
	return x+y

def mult(x, y):
	return (x * y)

def find_vals():
	for n in range(0, 99):
		for v in range(0, 99): 
			d = copy(data)
			grav_asst(n, v, d)
			if d[0] == address: 
				print(d[0], d[1], d[2])
			else:
				#print('vals', d[0])
				pass	

def grav_asst(n, v, rd):
	def rep_in(curr, t):
		try:
			rd[curr] = t
		except IndexError:
			pass
	rd[1] = n
	rd[2] = v
	i = 0
	while i < len(data):
		if rd[i] == 99: break
		else:
			x = rd[i+1]
			y = rd[i+2]
			if rd[i] == 1:
				s = add(rd[x], rd[y])
				c = rd[i+3]
				rep_in(c, s)
			elif rd[i] == 2:
				p = mult(rd[x], rd[y])	
				curr = rd[i+3]
				rep_in(curr, p)
		i += 4
	return rd[0]

find_vals()
#grav_asst(4, 6)
