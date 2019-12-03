path = './fuel-modules.txt'
mods = open(path, 'r')
m = mods.readline()
fuel = 0
c = 0
while m:
	fuel += (int(m)//3) - 2
	print(fuel)
	m = mods.readline()
print('total', fuel)
mods.close()
	
