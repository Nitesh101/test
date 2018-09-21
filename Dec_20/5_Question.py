#!/usr/bin/python
def count_words():
	num_words = 0
	fa = open("file2.txt","r")
	for index in fa:
		words = index.split()
		num_words += len(words)
	return  num_words
print count_words()
"""

def sum_numbers():
	sum_num = 0
	fa = open("file3.txt","r")
	for index in fa:
		num = index.split()
		sum_num += index
	return sum_num
print sum_numbers()
"""
