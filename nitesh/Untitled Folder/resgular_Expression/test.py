import sys
inp = raw_input("Enter a user input: ")
lst =inp.split()
print lst

N = 0
E = 0
S = 0
W = 0
for val in lst:
	if val[0] == "N":
		N += int(val[1])
	elif val[0] == "S":
		S += int(val[1])
	elif val[0] == "E":
		E += int(val[1])
	elif val[0] == "W":
		W += int(val[1])
if N == S and E == W:
	area = N * W 
	print area
print sys.argc[0]
