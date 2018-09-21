import os, time
def pipe():
	'''Pipes normally only let data flow in one direction -- one side is input, one is output.'''
	log=open("file.log","a")
	try:
		def child(pipeout):
    		zzz=0
    		while 1:
        		time.sleep(zzz)      
                os.write(pipeout, 'Spam %03d\n' % zzz)   
        		zzz = (zzz+1) % 5                        
         
		def parent(  ):
    			pipein, pipeout = os.pipe(  )   
    			if os.fork(  ) == 0:      
        			s.close(pipein)          
        			child(pipeout)
    			else: 
        			os.close(pipeout)   
	        		pipein = os.fdopen(pipein)       
        			while 1:
            				line = pipein.readline(  )[:-1]        
		parent(  )	
		log.write("pipe       PASS\n")
		log.close()
	except:
		log.write("pipe       FAIL\n")
		log.close()

if __name__=="__main__":
	pipe()
