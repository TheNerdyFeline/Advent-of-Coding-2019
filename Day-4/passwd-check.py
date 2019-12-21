# range 172930-683082
from operator import eq

pws = list(range(172930, 683083))

def pass_check(num_range):
	c = 0
	for i in num_range:
		i = str(i)
		if len(i) < 6:
			pass
		else:
			n = [int(d) for d in str(i)]
			if any(map(eq, i, i[1:])) and sorted(n) == n:
				c += 1
	print(c)

#pass_check(list(range(244567, 244667)))
pass_check(pws)
