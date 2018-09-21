import re
f = open('data.txt','r')
fa = f.read()
#Extract all the text from the file and print it 
#print fa
#Find and extract the year and print it 
#match = re.findall(r'\d{4}',fa)
#Extract the names and rank numbers and print them
#match = re.findall(r'\w+\s\d',fa)
#Get the names data into a dict and print it 
match = re.match(r'(\w+)',fa)
print match
