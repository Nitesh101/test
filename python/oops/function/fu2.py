def palindrome(string):
	if string == string[::-1]:
		print "the given string is polindrome"
	else:
		print "the given string is not polindrome"
palindrome('100001')
