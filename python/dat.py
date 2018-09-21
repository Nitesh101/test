a = [1, 2, 2, 1, 3, 4, 2, 1, 2, 5]
print max(a,key=a.count)
a = ['1', '2', '3', '7', '8', '9', '10']
print max(a,key=int)
a = [-1, -2, -3, 4, 5, -7, -6, -9]
print max(a,key=abs)
