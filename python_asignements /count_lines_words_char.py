num_lines = 0
num_words = 0
num_char = 0
fa = open('file2.txt','r')
for i in fa:
	words= i.split()
	num_lines  += 1
	num_words  += len(words)
	num_char += len(i)
print num_lines
print num_words
print num_char
