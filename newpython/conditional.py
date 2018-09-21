"""
val1 = raw_input("enter a string val1: ")
val1 = len(val1)
val2 = raw_input("enter a string val2: ")
val2 = len(val2)
if val1 > val2:
	print "The val1 is greater"
elif val2 > val1:
	print "The val2 is greater"
elif val1==val2:
	print "strings are equal"
else:
	print "not a strng"

val1 = input("enter a integer val1: ")
val2 = input("enter a ineger val2: ")
if val1 > val2:
	print "val1 is greater"
elif val2 > val1:
	print "val2 is greater"
elif val1 == val2:
	print "string are equal"
else:	
	print "not equal"

num = float(input("Enter a number: "))
if num >= 0:
	if num == 0:
		print ("zero")
	else:
		print("positive zero")
else:
	print("Negative number")
"""
while True:
	val1 = input("enter a  value: ")
	val2 = input("enter a value: ")
	condition = input("1sum\n2sub\n3div\n4mul\n5exit\n")
#while True:
	if condition == 1:
		print "The sum of two values: ",val1+val2
		break
	elif condition == 2:
		print "The substraction of two numbers: ",val1-val2
		break
	elif condition == 3:
		print "The div of two numbers: ",val1%val2
		break
	elif condition == 4:
		print "The mul of two numbers: ",val1*val2
		break
	else:
		print "enter correct input"
		#condition = input("enter")
	
		
