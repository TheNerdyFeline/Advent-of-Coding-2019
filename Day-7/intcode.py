import sys
import itertools
from copy import copy

data = sys.stdin.readline().split(',')
diag_codes = [int(d) for d in data]
#sys_id = 5

def intcode(diag, phase_setting, inp_sig):
	i = 0
	j = 0
	while True:
		def get_par(ps):
			m1 = diag[i]//100 % 10
			par1 = diag[i+1]
			p1 = diag[par1] if m1 == 0 else par1
			if ps == 3:
				m2 = diag[i]//1000 % 10
				par2 = diag[i+2]
				p2 = diag[par2] if m2 == 0 else par2
				par3 = diag[i+3]
				return(p1, p2, par3) 
			elif ps == 2:
				m2 = diag[i]//1000 % 10
				par2 = diag[i+2]
				p2 = diag[par2] if m2 == 0 else par2
				return(p1, p2)
			else:
				return(p1)
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
			phase = phase_setting
			inp = inp_sig
			if j == 0 : 
				diag[p1] = phase
				j += 1
			elif j == 1:
				diag[p1] = inp
			i += 2
		elif opcode == 4:
			output = get_par(1)
			#print('op4', output)
			return output
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

def run_amps(data, phase):
	inp_sig = 0
	for i in phase:
		d = copy(data)
		phase_set = i
		output = intcode(d, phase_set, inp_sig)	
		inp_sig = output
	return output

def get_highest(data):
	phases = [0, 1, 2, 3, 4]
	phase_perms = list(itertools.permutations(phases))
	highest = 0
	for p in phase_perms:
		output = run_amps(data, p)
		#print(output)
		if output > highest:
			highest = output
	print(highest)

#intcode(diag_codes)
get_highest(diag_codes)
# test = 43210
# test2 = 54321
# test3 = 65210
