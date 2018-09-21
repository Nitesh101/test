n = input("Enter a input: ")
l = input("Enter a start bit: ")
r= input("Enter a start bit: ")
n=int(n)
for i in range(l,r,2):
		n=n|1<<i
print n
