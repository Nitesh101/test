"""
for val in range(3):
	print val
for val in range(1,3):
	print val
for val in range(1,10,2):
	print val

ini_val = input("enter initial value: ")
final_val = input("enter final value: ")
inc_val=input("ini_val,final_val,inc_val: ")
for val in range(ini_val,final_val,inc_val):
	print val

string =raw_input("enter a string: ")
sub_string =raw_input("enter a substring: ")
if (sub_string in string):
	print sub_string,"is a substirng of",string
elif(sub_string not in string):
	print sub_string ,"is not a substring of",string

val1 = input("enter a list: ")
val2 = input("value to serched : ")
length = len(val1)
for index in range(length):
		if (val2==val1[index]):
			print "found value",index
			break
else:	
		print "not found"

val = input("enter a value: ")
if val >1:
	for i in range(2,val):
		if(val %i)==0:
			print(val,"is not a prime number")
			break
	else:	
		print(val,"is prime number")
val = input("enter a value: ")
while val >1:
		for i in range(2,val):
			if(val%i)==0:
				print(val,"is not a prime number")
				
		else:
			print(val,"is prime number")
			break

ran =input("enter a start :")
i=2
while i<ran:
		for j in range(2,i):
			if(i%j)==0:
				print(i,"is not prime number")
				i=i+1
				break
		else:
			print(i,"is prime number")
			i=i+1

val = input("enter value after 10: ") 
count = 0
while (val < 50):
		count += 1
		print val
		if(count == 5):
			val+=5
			count = 0
		val+=1

val = input("enter a list: ")
ele = input("enter break value: ")
for i in val:
	if ele == i:
		break
	else:
		print i

val = input("enter a list: ")
ele = input("enter break value: ")
for i in val:
	if ele == i:
		continue
	else:
		print i
cnt  = 0
val = raw_input("enter a string: ")
while(val!="quit"):
		cnt+=1
		val = raw_input("enter a string: ")
print cnt
"""

