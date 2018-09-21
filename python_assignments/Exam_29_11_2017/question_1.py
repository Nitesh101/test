import re
username = raw_input("Enter a username : ")
while True:
	if username > 5:
		print "username is taken pls enter password"
		password = raw_input("Enter a password: ")
		if len(password) > 6 and len(password) < 12:
			if re.match(r'[A-Z]*[a-z]*[@#$]*[0-9]*',password):
				print "you are Entered sucessfully"
			else:
				#print "password should contain at least uppercsae and onr lower case"
				#password = raw_input("Enter a password: ")
				print "you have Not succesfully created"
		else:
			print "password does not match"
		break
		
	else:
		print "not valide"
