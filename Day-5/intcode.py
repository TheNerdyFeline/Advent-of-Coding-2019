from numpy import loadtxt

data = loadtxt('input.txt', comments='#', dtype='int', delimiter=',', unpack=False)
sys_id = 1
#print(data[0])

def rep_in(loc, t):
		try:
			data[loc] = t
		except IndexError:
			pass

def op1(x, y, p):
	v = x + y
	rep_in(p, v)

def op2(x, y, p):
	v = (x * y)
	rep_in(p, v)

def op3(p, inp):
	rep_in(p, inp)

def op4(pos):
	return data[pos]
	
def intcode(diag):
	for i in diag:
		instruction = diag[i]
		print('i', instruction)
		if instruction <= 99:
			opcode = instruction
		else:
			inst = [int(d) for d in str(instruction)]
			opcode = inst[-1:]
		m1 = inst[-3:-2] or 0
		m2 = inst[-4: -3] or 0
			# 0 = position, 1 = immediate
		p1 = diag[i+1]
		p2 = diag[i+2]
		p3 = diag[i+3]
		if m1 == 0: p1 = diag[p1]
		if m2 == 0: p2 = diag[p2]
		if opcode == 99:
			break
		elif opcode == 1:
			op1(p1, p2, p3)
			i += 4
		elif opcode == 2:
			op2(p1, p2, p3)
			i += 4
		elif opcode == 3:
			op3(p1, p2, sys_id)
			i += 2
		elif opcode == 4:
			output = op4(p1, p2)
			print(output)
			i +=2
	print(diag[0])

intcode(data)
#find_vals()
#grav_asst(4, 6)
