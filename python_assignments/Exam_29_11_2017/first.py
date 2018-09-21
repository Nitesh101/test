import re
username = raw_input("Enter a username : ")
while True:
	if username > 5:
		print "username is taken pls enter password"
		password = raw_input("Enter a password: ")
		if len(password) > 6 and len(password) < 12:
				if len(password) < 8:
            		print("Make sure your password is at lest 8 letters")
        		elif re.search('[0-9]',password) is None:
            		print("Make sure your password has a number in it")
        		elif re.search('[A-Z]',password) is None: 
            		print("Make sure your password has a capital letter in it")
        		else:
            		print("Your password seems fine")
           			break

		else:
			print "password does not match"
		
	else:
		print "not valide"
