a = [1,13,7,5,9]
for val in a:
	for v1 in a:
		if val != v1:
			if val+v1 == 14:
				print a.index(val),val
