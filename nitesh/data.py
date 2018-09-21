import re
val = ["abcd123 abcdewwe bcdd123 abcd 123 12345"]
for i in val:
	if re.match(r'^[a-z 0-9]$',i):
		print i
