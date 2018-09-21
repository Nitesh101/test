#!/usr/bin/python
from itertools import combinations

string=input("Enter string in binary form:")
integer =int(string)
length=len(string)
temp=list(string)

for num in combinations(temp,3):
		print int(''.join(num))
		
	





