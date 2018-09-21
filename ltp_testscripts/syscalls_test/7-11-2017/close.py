import os,sys

def close():
	'''closing function'''
    	log = open("file.log","a")
    	try:
			fname = os.open("new.txt", os.O_RDWR|os.O_CREAT)
			os.write(fname,"some data")
        		os.close(fname)
        		log.write("close    PASS\n")
        		log.close()
			fname.close()
    	except:
        	log.write("close    FAIL\n")
        	log.close()  
print close() 
