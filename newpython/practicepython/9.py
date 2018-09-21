import csv
"""
file = open('/home/madisnit/Desktop/new.csv','rb')
for line in file:
	print line
"""
file1 = csv.writer(open("nietsh.csv","wb"))
file1.writerow(["Name","Address","Telephone","Fax","E-mail","others"])
print file1
