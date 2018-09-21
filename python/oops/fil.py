import os,shutil
source = "/home/madisnit/Downloads/archive"
des = "/home/madisnit/Downloads/archive(1)"
for files in source:
	if files.endswith(".xlsx"):
		shutil.move(files,des)
