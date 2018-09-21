import os,sys
fd = os.open("test.txt",os.O_RDWR|os.O_CREAT)
d_fd = os.dup(fd)
os.write(d_fd,"This is test")
os.closerange(fd,d_fd)
print "change all the files successfully"
