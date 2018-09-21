dict = {"nitesh":{"val":[1,2,3,4]}}
print dict['nitesh']['val'][3]
print [j[3] for i in dict.values() for j in i.values()]
#for i in dict.values:
#	for j in i:
		
