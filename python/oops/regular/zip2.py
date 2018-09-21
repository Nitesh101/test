import os,zipfile
import shutil
if not os.path.exists('/home/madisnit/Desktop/oops/regular/another'):
    	os.makedirs('/home/madisnit/Desktop/oops/regular/another')
		os.move("/home/madisnit/Desktop/oops/regular/","/home/madisnit/Desktop/oops/regular/another")
elif:
	zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('/home/madisnit/Desktop/oops/regular/new', zipf)
    zipf.close()
	

