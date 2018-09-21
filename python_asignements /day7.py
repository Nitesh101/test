#!/usr/bin/python
"""
import sys,getopt

def main(argv):
	inputfile = ''
	outputfile = ''
	try: 
		opts,args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'getopts_test.py -i <inputfile> -o <ouputfile>'
		sys.exit(2)
	for opt,arg in opts:
		if opt == '-h':
			print 'usage: getopts_test.py -i<inputfile> -o<outputfile>'
			sys.exit()
		elif opt in ("-i","__ifile"):
			inputfile= arg
		elif opt in ("-o","__ofile"):
			outputfile = arg
	print 'input file  is ',inputfile
	print 'output file is',outputfile
	return
if __name__ == '__main__':
	main(sys.argv[1:])
 
import csv
fa = open("file.csv","rb")
readcsv = csv.reader(fa)
for row in readcsv:
	print row

while True:
	val = raw_input("Enter a string: ")
	fo = open("file.txt","a")
	fo.write(val)
	fo.write("\n")
	if val == "end":
		exit()
"""
def Emp_data(name):
		fo = open("employee.txt","r")
		fa=fo.readlines()
		for index in fa:
			lines=index.split(":")
			if lines[0] == name:
				print lines[0],":",lines[1]
		fo.close()
def main():
	name = raw_input("Enter a employee name: ")
	Emp_data(name)
main()	
