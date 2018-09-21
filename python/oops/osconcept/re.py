import re
for test_string in ['555-1212','ILL-EGAL']:
	if re.match(r'^\d{3}-\d{4}$','{A_Z}-{A-z}',test_string):
		print test_string,'is a valid user'
	else:
		print test_string,'rejected'
