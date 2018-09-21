#!/usr/bin/python
import sys,getopt
import os

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
			sys.exit(2)
		elif opt in ("-i","__ifile"):
			inputfile= arg
		elif opt in ("-o","__ofile"):
			outputfile = arg
	print 'input file  is ',inputfile
	print 'output file is',outputfile
	fo = open(inputfile,"w")
	fo.write("abc\n")
	fo.write("def\n")
	fo.write("ghi\n")
	fo.close()
	fo = open(inputfile,"r")
	fo.seek(0)
	lines=fo.readlines()
#	for line in lines:	
#		sum1=line
#	print sum1
	fo.close()
	fo=open(outputfile,"w+")
	for i in lines:
		fo.write("the line number is \n")
		fo.write(i)
	fo.close()
if __name__ == "__main__":
	main(sys.argv[1:])
