tot=input("Enter the number : ")
mid=tot/2
count=0
li=[]
for i in range(1,mid+2):
	siri=""
	for j in range(i):
		h=int(2**count)
		siri=siri+str(h)+" "
		count+=1
	li.append(siri)
li=li+li[-2::-1]
for i in li:
	print i,"\n"
