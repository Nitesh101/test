import shutil
import os
source = os.listdir("/home/madisnit/Desktop/nitesh")
destination = ("/home/madisnit/Desktop/nitesh/new")
for files in source:
	if files.endswith(".pptx"):
		shutil.move(files,destination)
