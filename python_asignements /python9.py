import re
username = raw_input("Enter a username : ")
while True:
	if len(username) > 5:
		print "username is taken pls enter password"
		password = raw_input("Enter a password: ")
		if len(password) > 6 and len(password) < 12:
			if re.match(r'((?=.*[A-Z])(?=.*[a-z])(?=.*[@#$%])(?=.*\d))',password):
				print "you are Entered sucessfully"
				break
			else:
				print "password should contain one special symbal(@,#,&,!) and one numbers"
				password = raw_input("Enter a password: ")
		
	else:
		print "not valide"
		username=raw_input("Enter again a username: ")
