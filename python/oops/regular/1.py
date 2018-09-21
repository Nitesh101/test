import re
text = 'alice-b@google.com ,nitesh@gmail.com'
match = re.findall(r'@\w+.\w+',text)
print match
