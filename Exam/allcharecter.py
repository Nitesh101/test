lines = []
while True:
	l = input("enter a value: ")
	if l:
		lines.append(l.upper())
	else:
		break
for l in lines:
	print l
