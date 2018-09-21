def string_len(str1):
	if len(str1) < 2:
		return ''
	return str1[0:2] + str1[-2:]
print string_len('w3dfhdajkbda')
print string_len('e')
