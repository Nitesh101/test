def get_string(str1):
	char = str1[0]
	length = len(str1)
	str1 = str1.replace(char,'$')
	str1 = char + str1[1:]
	return str1
print get_string('restart')
