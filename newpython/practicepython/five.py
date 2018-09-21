import os
import shutil
# make sure that these directories exist
dir_src = "/home/madisnit/Desktop/nitesh"
dir_dst = "/home/madisnit/Desktop/nitesh2"
for file in os.listdir(dir_src):
	src_file = os.path.join(dir_src, file)
	dst_file = os.path.join(dir_dst, file)
	shutil.move(src_file, dst_file) 
