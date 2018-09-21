import os,time
import datetime
def rtc():
	'''Real Time Clock, they usually mean something that tracks wall clock time and is battery backed so that it works even with system power off. '''
	log = open("file.log","a")
	try:
   		now = datetime.datetime.now()
		#while True:
		now.strftime("%Y-%m-%d %H:%M")
		log.write("rtc       PASS\n")
		log.close()
	except:
		log.write("rtc        FAIL\n")
		log.close()
if __name__=="__main__":
	rtc()
