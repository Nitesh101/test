import fnmatch
import os
 
rootPath = '/home/madisnit/Desktop/oops'
pattern = 'highestNumber'
 
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print( os.path.join(root, filename))
