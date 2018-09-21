def max(x,y):
	if x >y :
		return x
	return y
def max_of(x,y,z):
	return max(x,max(y,z))
print max_of(8,9,10)
