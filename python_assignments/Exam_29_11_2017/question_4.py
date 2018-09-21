#!/usr/bin/python
move=raw_input("Enter movement:")
new_move=move.split(',')
distance=[]
up=int(input("Enter input UP: "))
down=int(input("Enter input DOWN: "))
left=int(input("Enter input LEFT: "))
ryt=int(input("Enter input RIGHT: "))

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
	
