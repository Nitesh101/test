l = []
while True:
	val = input()
	if val:
		l.append(val.upper())
	else:
		break
for val in l:
	print val
