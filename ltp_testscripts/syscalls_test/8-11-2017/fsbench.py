import os
def fsbench():
	''' It reports benchmarks in the form of elapsed times for several individual tests,for which file sizes, chunk sizes, and random seek counts can be
specified on the command line'''
	log = open("file.log","a")
	try:
		os.path.getsize("/home/madisnit/Desktop/syscalls_test/8-11-2017/new.txt")
		log.write("fsbench     PASS\n")
		log.close()	
	except:	
		log.write("fsbench     FAIL\n")
		log.close()
if __name__=="__main__":
	fsbench()
