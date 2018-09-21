import os
def getcwd():
	'''Return a string representing the current working directory'''
	log = open("file.log","a")
	try:
		os.getcwd()
		log.write("getcwd  PASS\n")
		log.close()
	except:
		log.write("getcwd  FAIL\n")
		log.close()
if __name__=="__main__":
	getcwd()
