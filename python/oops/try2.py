def this_fails():
	x = 1/10
try:
	this_fails()
except ZeroDivisionError as detail:
	print "handling run-time error: ",detail
