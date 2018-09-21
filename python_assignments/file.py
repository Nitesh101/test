import os
for root,dirs,files in os.walk('/home/madisnit/Desktop/oops'):
#	print root
#	print dirs
	for name,roots,files in files:
		val = raw_input("Enter a string you want: ")
		if val == name:
 			print dirs
			print root
			print val
