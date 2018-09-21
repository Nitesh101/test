import re
f = open("new.txt","r")
fa = f.read()
match = re.findall(r'(\d{3})-(\d{3})-(\d{4})',fa)
print match
