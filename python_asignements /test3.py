#!/usr/bin/python
def comman_ele(lis1,lis2):
	res=[]
	for ele in lis1:
		if ele in lis2:
			res.append(ele)
	return res
print comman_ele([2,3,4,5],[2,4,1,6,7])

def val():
	start = 1
	stop = 100
	for num in range(start,stop+1):
		if num > 1:
			for i in range(2,num):
				if num%i == 0:
					print num,"is not prime numbers"
					break
			else:
				print num,"prime numbers"

val()