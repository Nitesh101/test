v1 = 0xCD
print bin(v1)
val=input("Enter the position you want to set: ")
var=0x1<<val
d=v1|var
print bin(d)
v2 = 0xCD
print bin(v2)
val=input("Enter the position you want to clear: ")
var2=~(0x01<<val)
c=v2&var2
print bin(c)
