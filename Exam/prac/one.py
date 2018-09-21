import os
import shutil
src = '/home/madisnit/Desktop/Exam/prac'
dst = '/home/madisnit/Desktop/Exam/'
for files in src:
	shutil.move(files,dst)
