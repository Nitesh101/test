def new_string(str):
	if len(str) >= 2 and str[:2] == "IS":
		return str
	return "IS"+str
print (new_string("Array"))
print(new_string("Array")) 
