print("Enter :\n1.Add\n2.Mul\n3.Sub\n4.Div\n5.exit\n")
opt=input("Enter input  option:")
val1=input("Enter input val1:")
val2=input("Enter input val2:")
while True:
	if (opt==1):
		print val1+val2
		break
	elif opt==2:
		print val1*val2
		break
	elif opt==3:
		if val1>val2:
			print val1-val2
		else:
			print val2-val1
	elif opt==4:
		print val1/val2
	elif opt==5:
		print val1%val2
	else:
		print "Enter valid option"
