import os,sys
import uuid
def linktest():
	'''  A regression test for links per file.
                    Linktest.pl is a simple test that attempts
                    to create a given number of hard links and
                    symbolic links to a single file.'''
	log = open("file.log","a")
	try:
		
		random_unique_name = str(uuid.uuid4()) + str(uuid.uuid1())


		def find_mount_point(path):  # http://stackoverflow.com/questions/4453602/how-to-find-the-mountpoint-a-file-resides-on
    			path = os.path.abspath(path)
    			while not os.path.ismount(path):
        			path = os.path.dirname(path)
    			return path

		for root, dirs, files in os.walk(os.getcwd()):
    			for name in files:
        			fullname = os.path.join(root, name)
        			tempname = os.path.join(root, random_unique_name)
        			if os.path.islink(fullname):
            				linkpath = os.readlink(fullname)
            			if (find_mount_point(fullname) == (find_mount_point(os.path.split(linkpath)[0]))):
               	 			print "%s links to %s" % (fullname, linkpath)
                # Rename current link to something temporary
                			os.rename(fullname, tempname)
                			try:
                    # Try to create hard link for the file
                    				os.link(linkpath, fullname)
                    # If we succeeded, remove temporary file
                    				os.unlink(tempname)
                    				print "Created  hardlink for %s" % fullname
                			except:
                    # If we failed, rename the temporary file back, and abort with some meaningful info
                    				e = sys.exc_info()[0]
                    				sys.stderr.write("Hardlinking failed on %s, aborting !" % fullname)
                    				os.rename(tempname, fullname)
                    				sys.exit(e)
            			else:
								print "%s on other FS!" % name
		log.write("linktest      PASS\n")
		log.close()
	except:
		log.write("linktest       FAIL\n")
		log.close()

if __name__=="__main__":
	linktest()
