def putNumbers(n,limit):
    i = 1
    while i<limit:
        if i%n==0:
            yield i
	i+=1
n=input("Enter a value: ")
limit=input("Enter a value: ")
for i in putNumbers(n,limit):
	print i
