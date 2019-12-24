import sys

data = sys.stdin.readline().split(',')
diag_codes = [int(d) for d in data]
sys_id = 1

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
			v = p1 + p2
			diag[p3] = v
			i += 4
		elif opcode == 2:
			p3 = diag[i+3]
			p1, p2 = get_par()
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

intcode(diag_codes)
# 3 not right
