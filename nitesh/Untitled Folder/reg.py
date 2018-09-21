import re 
f = open("reslt.txt")
fa = f.readline()
fb=re.findall(r"results",fa)
print fb

