item = []
num = [x for x in input().split(',')]
for p in num:
	x = int(p,2)
	if not x%5:
		item.append(p)
print items
