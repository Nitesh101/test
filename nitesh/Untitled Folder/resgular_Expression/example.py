import re
s=""
with open("file.txt","r+") as f:
    data = f.readlines()
    for i in data:
        rep=re.sub("test","test",i)
        s=s+rep
    f.seek(0)
    f.write(s)
