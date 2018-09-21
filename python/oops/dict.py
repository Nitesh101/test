#!/usr/bin/python
dict = {"name" : {"nitesh":[1,2,3,4]}}
print dict["name"]
"""
for i in dict.values():
	for j in i.values():
		print j[2]
"
dict["name"] = "roja"
print dict

v = {"ram": 34, "bush":23, "john":12}
val = sorted(v.items(), key=v.get)
print val
lst = [(1, 3, 4), (3, 2, 5), (2, 1, 3), (7, 7, 2)]
val = [lst[-1],lst[-2],lst[0],lst[1]]
print val
"""
