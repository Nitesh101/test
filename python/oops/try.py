"""
try:
	doSomething()
except:
	pass

try:
	something here()
except:
	print "the whatever error occured"

import traceback
try:
	raise TypeError("oops!")
except Exception, err:
	try:
		raise TypeError("Agau=in !?!")
	except:
		pass
tarceback.print_exc()
"""
while True:
	try:
		x = int(input("please enter a number: "))
		break
	except ValueError:
		print "Oops that was"
	
