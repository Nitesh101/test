import shutil
import os
import glob
val = glob.iglob(os.path.join('/home/madisnit/Desktop/nitesh','*.pptx'))
for files in val:
	if os.path.isfile(files):
		shutil.move(files,'/home/madisnit/Desktop/venu')
