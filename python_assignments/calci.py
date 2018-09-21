#!/usr/bin/python


print("Enter :\n 1.Add\n 2.Mul\n 3.Sub\n 4.Div\n 5.Mod\n")
opt=input("Enter input  option:")
val1=input("Enter input val1:")
val2=input("Enter input val2:")

if (opt==1):
	print val1+val2
elif opt==2:
	print val1*val2
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
