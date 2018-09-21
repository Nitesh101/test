import os,sys
def stat_float_time():
	''' Determine whether os.[lf]stat represents time stamps as float objects.
        If newval is True, future calls to stat() return floats, if it is False,
        future calls return ints. 
        If newval is omitted, return the current setting.
'''
	log = open("file.log","a")
	try:
		statinfo = os.stat("popen.py")
		statinfo = os.stat_float_times()
		log.write("stat_float_times   PASS\n")
		log.close()
	except:
		log.write("stat_float_times    FAIL\n")
		log.close()
if __name__=="__main__":	
	stat_float_time()
