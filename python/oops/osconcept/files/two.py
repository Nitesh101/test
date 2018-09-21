def append(fname):
	from itertools import islice
	with open(fname,"w") as f:
		f.write("python Exercise\n")
		f.write("java Exercise\n")
	txt = open(fname)
	print(txt.read)
print append("val.txt")
	
