import re
contactInfo = 'Doe, John: 555-1212'
search = re.search(r'(\w+),(\w+): (\s+)',contactInfo)
print search.group(1)
