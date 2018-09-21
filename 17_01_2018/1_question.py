#!/usr/bin/python
val2 = int(input("Enter which position prime you want: "))
num = 2
total = 0
while total!= val2:
	for i in range(2,num):
		if num%i == 0:
			num += 1
			break
	else:
		num += 1
		total += 1
print "prime number is position {} is {}.".format(val2,num-1)
