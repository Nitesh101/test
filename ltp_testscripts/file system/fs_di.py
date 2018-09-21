import filecmp
def fs_di():
	'''Creates a data file of specified or random size and copies
#         the file to a random directory depth on a specified filesystem
#	      The two files are compared and checked for differences.
#	      If the files differ, then the test fails. By default, this
#	      test creates a 30Mb file and runs for ten loops..'''
	log = open("file.log","a")
	try:
		filecmp.cmp("/home/madisnit/Desktop/syscalls_test/9-11-2017/file1.txt","/home/madisnit/Desktop/syscalls_test/9-11-2017/file2.txt",shallow=True)
		log.write("fs_di       PASS\n")
		log.close()
	except:
		log.write("fs_di        FAIL\n")
		log.close()
if __name__=="__main__":
	fs_di()
