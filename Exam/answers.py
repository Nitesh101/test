"""
import os,shutil
sur = os.listdir("/home/madisnit/Desktop")
print sur
des = os.listdir("/home/madisnit/Downloads")
print des
shutil.move(sur,des)
"""
import os
import shutil
# make sure that these directories exist
dir_src = os.listdir("/home/madisnit/Desktop/nitesh")
print dir_src
dir_dst = "/home/madisnit/Downloads" 
for file in dir_src:
  #  print file 
	if file.endswith(".txt"):
		src_file = os.path.join(dir_src,file)
		dst_file = os.path.join(dir_dst,file)
		shutil.copy(dir_src,dir_dst)
