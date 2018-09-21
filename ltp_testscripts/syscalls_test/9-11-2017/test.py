import os
try:
    f = open("file.txt", "w")
except IOError:
    pass
 
# Remove a file.
try:
    os.remove("file.txt")
except os.error:
    pass
 
