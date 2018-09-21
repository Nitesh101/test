import random
val = random.randint(20,30)
lst = []
for index in range(val):
	tmp = random.randint(-15,15)
	lst.append(tmp)
print lst
positive_lst = filter(lambda x: x > 0,lst)
print "positive numbers in list",positive_lst
cube_lst = map(lambda x:x**3,positive_lst)
print "cube of list",cube_lst
sum_of_cube = reduce(lambda x,y:x+y, cube_lst)
print "sum of cubes of numbers",sum_of_cube
