import operator
a = []
a.append(["Nick", 30, "Doctor"])
a.append(["John",  8, "Student"])
a.append(["Paul", 22, "Car Dealer"])
a.append(["Mark", 66, "Retired"])
#a.sort(key=operator.itemgetter(1))
a.sort(key=lambda a:a[2])
print a
