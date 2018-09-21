"""
#1
val = input("enter a valuse : ")
#d = {}
print tuple(val)
print list(val)
#print dict(val)

#2
val = input("enter a strin : ")
print (val)

#3
x = 1
print eval('x+1')
print eval('x')

dec = 34
print dec
print (bin(dec))
print (oct(dec))
print (hex(dec))
#3
binary = raw_input("enter a binary value: ")
val = int(binary,2)
print  ("The convrtion of binary to decimal value is:",int(val))
print ("The convrtion of binary to octal value is: ",oct(val))
print ("The convertion of binary to hexdecimal value is",hex(val))

hex_decimal = raw_input("enter a hexdecimal value: ")
#print ("The convertion of hexadecimal to ocatal: ",oct(hex_decimal))
print ("The convertion of hexdecimal to binary:",bin(hex_decimal))
"""

val = input("enter  a binary number: ")

print int(val)
print oct(val)
print hex(val)

val = input("enter a decimal number: ")
print bin(val)
print hex(val)
print oct(val)
val = input("enter a hexdecimal value: ")
print int(val)
print bin(val)
print oct(val)
val = input("enter a octal value: ")
print int(val)
print bin(val)
print hex(val)
