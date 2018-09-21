import os
def fsstress():
	'''When we did some permutation and combination in the operations listed in fsstress ,
found that when 'symlink' operation is taken out from the execution list of fsstress.
Everthing goes fine with the same setup.
'''
	log = open("file.log","a")
	try:
		src = '/usr/bin/python'
		dst = '/tmp/python'
		os.symlink(src,dst)
		log.write("fsstress       PASS\n")
		log.close()
	except:
		log.write("fsstress        FAIL\n")
		log.close()
if __name__=="__main__":
	fsstress()
