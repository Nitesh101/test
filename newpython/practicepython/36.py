import re
val =  open('/home/madisnit/Desktop/practicepython/new.txt','r') 
content = val.readlines()
text = re.search(r'/(.*cow\s+)(.*)(\s+milk.*)/;', content)
print text
