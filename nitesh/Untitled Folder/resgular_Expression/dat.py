import re
str = raw_input("Enter the string: ")
re = re.search(r'^[A-Z a-z 0-9]',str)
print re.group()
