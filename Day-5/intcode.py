import sys

data = sys.stdin.readline().split(',')
diag_codes = [int(d) for d in data]
sys_id = 1

def rep_in(a, v):
		try:
			diag_codes[a] = v
		except IndexError:
			pass

def op1(x, y, p):
	v = x + y
	#print(v)
	rep_in(p, v)

def op2(x, y, p):
	v = (x * y)
	rep_in(p, v)

def op3(p, inp):
	rep_in(p, inp)

def op4(pos):
	return diag_codes[pos]
	
def intcode(diag):
	i = 0
	while i < len(diag):
		def get_par():
			m1 = diag[i]//100 % 10
			m2 = diag[i]//1000 % 10
			par1 = diag[i+1]
			par2 = diag[i+2]
			p1 = diag[par1] if m1 == 0 else par1
			p2 = diag[par2] if m2 == 0 else par2
			return(p1, p2)
		opcode = diag[i] % 100
		if opcode == 99:
			break
		elif opcode == 1:
			p3 = diag[i+3]
			p1, p2 = get_par()
			#print('op1', p1, p2, p3)
			op1(p1, p2, p3)
			i += 4
		elif opcode == 2:
			p3 = diag[i+3]
			p1, p2 = get_par()
			op2(p1, p2, p3)
			i += 4
		elif opcode == 3:
			p1 = diag[i+1]
			op3(p1, sys_id)
			i += 2
		elif opcode == 4:
			p1 = diag[i+1]
			output = op4(p1)
			print('op4', output)
			i +=2

intcode(diag_codes)
# 3 not right
