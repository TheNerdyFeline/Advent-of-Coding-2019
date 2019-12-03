tf = 3394032
cf = 0
cm = 3394032

while cm > 8:
	#print('cm', cm)
	cm = (cm//3) - 2
	cf += cm
	print('cm', cm, 'cf', cf)

print(cf, cf+tf)
