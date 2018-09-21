f = open('file.txt','r')
filea = f.readlines()
print filea
variable = raw_input('which is varible you want \n')

if variable in ("AX", "AY", "AZ"):
	if variable == "AX":
		result = filea[0].split()[3]
		print result
	elif variable == "AY":
		result = filea[0].split()[4]
		print result
	elif variable == "AZ":
		result = filea[0].split()[5]
		print result
elif variable in ("MX", "MY", "MZ"):
	if variable == "MX":
		result = filea[1].split()[3]
		print result
	elif variable == "MY":
		result = filea[1].split()[4]
		print result
	elif variable == "MZ":
		result = filea[1].split()[5]
		print result
elif variable in ("OX", "OY", "OZ"):
	if variable == "OX":
		result = filea[2].split()[3]
		print result
	elif variable == "OY":
		result = filea[2].split()[4]
		print result
	elif variable == "OZ":
		result = filea[2].split()[5]
		print result
else:
	print "Unknown"

fo.close()
