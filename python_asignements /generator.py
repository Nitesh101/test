"""
def divi(n):
	for i in range(0,n):
		if i % 7 == 0:
			yield i
for val in divi(1000):
	print val,
"""
for i in range(0,1000):
	if i % 7 == 0:
		print i,

