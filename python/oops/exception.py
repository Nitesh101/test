def divide(x,y):
	try:
		result = x / y
	except TypeError:
		print "division by Zero"
	else:
		print "result is",result
	finally:
		print "executing finally "
divide(2,0)
