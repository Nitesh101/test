import csv
with open('some.csv','r') as f:
	reader = csv.reader(f)
	for row in reader:
		print row
