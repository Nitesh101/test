#!/usr/bin/python
move=raw_input("Enter movement:")
new_move=move.split(',')
distance=[]
up=0
down=0
left=0
ryt=0

for string in new_move:
	if (string[0:2]=='UP'):
		up+=int(string[2:])
	elif (string[0:4]=='DOWN'):
		down+=int(string[4:])
	elif (string[0:4]=='LEFT'):
		left+=int(string[4:])
	elif (string[0:5]=='RIGHT'):
		ryt+=int(string[5:])

distance.append(up-down)
distance.append(ryt-left)
print "Distance :",distance
	
