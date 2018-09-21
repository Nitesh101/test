import os, sys, stat

# Assuming /tmp/foo.txt exists, Set a file execute by the group.
os.chmod("/home/madisnit/Desktop/syscalls_test/foo.txt", stat.S_IXGRP)

# Set a file write by others.
os.chmod("/home/madisnit/Desktop/syscalls_test/foo.txt", stat.S_IWOTH)
print "Changed mode successfully!!"
