import os, sys

# Open a file
path = "/home/madisnit/Desktop/file.py"
fd = os.open( path, os.O_RDWR|os.O_CREAT )

# Close opened file
os.close( fd )

# Now create another copy of the above file.
dst = "/home/madisnit/Downloads/file.py"
os.link( path, dst)

print "Created hard link successfully!!"
