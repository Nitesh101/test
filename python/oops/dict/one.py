d = dict()
d['xyz'] = 123
d['abc'] = 345
print d
for index,value in enumerate(d):
	print index,value, d[value]
del d['xyz']
print d
