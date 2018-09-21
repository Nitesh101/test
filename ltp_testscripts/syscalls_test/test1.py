import os, sys, stat

# Now open a file "/tmp/foo.txt"
fd = os.open( "/home/madisnit/Desktop/syscalls_test/test.txt", os.O_IROTH )

# Set a file execute by the group.

os.fchmod( fd, stat.S_IROTH)

# Set a file write by others.
os.fchmod(fd, stat.S_IWOTH)

print "Changed mode successfully!!"

# Close opened file.
os.close( fd )
