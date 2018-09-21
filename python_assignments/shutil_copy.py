import os
src = os.listdir("/home/madisnit/Desktop/oops")
lis = []
lis2 = []
for file in src:
	if file.endswith(".py"):
		lis.append(file)
	elif file.endswith(".txt"):
		lis2.append(file)
file_name=os.path.join("/home/madisnit/Desktop/oops",lis)
shutil.copy("/home/madisnit/Documents/oops",file_name)
#print "list of python files: ",lis
#print "list of text file: ",lis2
