import sys

data = sys.stdin.readline().split(',')
diag_codes = [int(d) for d in data]
sys_id = 5

def intcode(diag):
	i = 0
	while True:
		def get_par(ps):
			m1 = diag[i]//100 % 10
			m2 = diag[i]//1000 % 10
			par1 = diag[i+1]
			par2 = diag[i+2]
			par3 = diag[i+3]
			p1 = diag[par1] if m1 == 0 else par1
			p2 = diag[par2] if m2 == 0 else par2
			if ps == 3:
				return(p1, p2, par3) 
			else:
				return(p1, p2)
		opcode = diag[i] % 100
		if opcode == 99:
			break
		elif opcode == 1:
			p1, p2, p3 = get_par(3)
			v = p1 + p2
			diag[p3] = v
			i += 4
		elif opcode == 2:
			p1, p2, p3 = get_par(3)
			v = p1 * p2
			diag[p3] = v
			i += 4
		elif opcode == 3:
			p1 = diag[i+1]
			diag[p1] = sys_id
			i += 2
		elif opcode == 4:
			p1 = diag[i+1]
			output = diag[p1]
			print('op4', output)
			i +=2
		elif opcode == 5:
			p1, p2 = get_par(2)
			if p1 != 0: 
				i = p2 
			else:
				i += 3
		elif opcode == 6:
			p1, p2 = get_par(2)
			if p1 == 0: 
				i = p2 
			else:
				i += 3
		elif opcode == 7:
			p1, p2, p3 = get_par(3)
			diag[p3] = 1 if p1 < p2 else 0
			i += 4
		elif opcode == 8:
			p1, p2, p3 = get_par(3)
			diag[p3] = 1 if p1 == p2 else 0
			i += 4

intcode(diag_codes)
