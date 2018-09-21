while True:
	val = raw_input("Enter a string: ")
	fo = open("file.txt","a")
	fo.write(val)
	fo.write("\n")
	if val == "end":
		exit()
	
