import os
import shutil
src_dir = "/home/madisnit/Desktop/nitesh"
dst_dir = "/home/madisnit/Desktop/nitesh2"
for file in os.listdir(src_dir):
	print file
	src_file = os.path.join(src_dir,file)
	dst_file = os.path.join(dst_dir,file)
	shutil.move(src_file,dst_file)
