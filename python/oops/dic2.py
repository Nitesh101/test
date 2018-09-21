"""
color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}
for key in sorted(color_dict):
	print key,color_dict[key]

	
student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}

for keys,values in student_data.items():
	if values not in student_data.items():
		print keys,values
	elif keys not in values.items():
		print keys,values

from heapq import nlargest
d = {'a':500, 'b':555,'c':3333}
three = nlargest(3,d,key=d.get)
print three

from collections import defaultdict,Counter
str1 = 'w3resource'
d = {}
for x in str1:
	d[x]= d.get(x,0)+1
print d
"""
num = [1,2,3,4]
new = current = {}
for name in num:
	current[name] = {}
	current = current[name]
	
print new

