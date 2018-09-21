import re
str = 'an example word:cat!!'
match = re.search(r'word:^[a-z]$',str)
print match.group()
