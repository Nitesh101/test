import os

for i,j,k in os.walk("/"):
	if ".pyc" in k:
		os.system("sudo rm k")

