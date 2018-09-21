fa = open("employee.txt","r")
fo=fa.readlines()
for index in fo:
	lines = index.split(":")
	if lines[0] == emp_name:
		print lines[0] ," : ",lines[1]
		emp_name = raw_input("Enter a employee name: ")
