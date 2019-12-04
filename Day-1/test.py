import sys

total = 0
for line in sys.stdin:
	print('test')
	fuel = int(line)//3 - 2
	while fuel > 0:
		total += fuel
  	fuel = fuel//3 - 2
print(total)
