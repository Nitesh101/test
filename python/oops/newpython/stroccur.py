def string_char(str1):
	char=str1[0]
	lenght=len(str1)
	str1=str1.replace(char,'$')
	str1=char+str1[1:]
	return str1
print(string_char('restart'))
