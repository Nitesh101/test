#!/usr/bin/python
#fb= "file2.txt"

num_lines = 0
num_words = 0
num_chars = 0

fa = open("file2.txt","r")
for line in fa:
	words = line.split()

	num_lines += 1
    	num_words += len(words)
    	num_chars += len(line)
print num_chars
print num_words
print num_lines
