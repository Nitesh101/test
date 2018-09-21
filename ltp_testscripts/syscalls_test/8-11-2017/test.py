import os, sys

# Open a file
fd = os.open( "/home/madisnit/Desktop/syscalls_test/8-11-2017/new.txt", os.R_OK)

# Now get  the touple
info = os.fstat(fd)

print "File Info :", info

# Now get uid of the file
print "UID of the file :%d" % info.st_uid

# Now get gid of the file
print "GID of the file :%d" % info.st_gid

# Close opened file
os.close( fd)
