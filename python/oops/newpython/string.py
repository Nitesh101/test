def string_char(str1):
	if len(str1) < 2:
		return ' '
	return str1[0:2] + str1[-2:]
print(string_char('w3reource'))
