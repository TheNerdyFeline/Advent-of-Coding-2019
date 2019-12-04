from numpy import loadtxt
data = loadtxt('data.txt', comments='#', dtype='int', delimiter=',', unpack=False)
#data = [1, 1, 1, 4, 99, 5, 6, 0, 99]
#print(data)

def add(x, y):
	return x+y

def mult(x, y):
	return (x * y)

def rep(c, t):
	try:
		data[c] = t
	except  IndexError:
		pass

def find_vals():
	for n in range(0, 9):
		for v in range(0, 9): 
			grav_asst(n, v)
			if data[0] == 19690720: 
				print(data[0], data[1], data[2])
			else:
				print(n, v, data[0])
				break

def grav_asst(n, v):
	data[1] = n
	data[2] = v
	i = 0
	while i < len(data):
		if data[i] == 99: break
		else:
			x = data[i+1]
			y = data[i+2]
			if data[i] == 1:
				s = add(data[x], data[y])
				c = data[i+3]
				rep(c, s)
			elif data[i] == 2:
				p = mult(data[x], data[y])	
				curr = data[i+3]
				rep(curr, p)
		i += 4
	print(data[0])
	return data[0]

find_vals()
#grav_asst(52, 6)
