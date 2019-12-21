# range 172930-683082
from operator import eq
from itertools import groupby

pws = list(range(172930, 683083))
pp = []

def pass_check(num_range):
	c = 0
	for i in num_range:
		i = str(i)
		if len(i) < 6:
			pass
		else:
			n = [int(d) for d in i]
			if any(map(eq, i, i[1:])) and sorted(n) == n:
				pp.append(n)
				c += 1
	print('pc1', c)
	pass_check2(pp)

def pass_check2(a):
	c = 0
	for j in a: 
		runs = [len(list(g)) for _, g in groupby(j)]
		for r in runs:
			if r == 2:
				rs = sum(u for u in runs if u > 1)
				c += 1
				break
	print(c)

pass_check(pws)
# 1675, 1142
