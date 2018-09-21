#!/usr/bin/python
def prime_num(inp):
        for val in range(2,(inp/2)+1):
                if (inp%val==0):
                        print "%d is not a prime number"%inp
                        break
        else:
                print "%d is prime number"%inp

inp=input("Enter the input number :")
def prime_list(inp1=1,inp2=100):
        l=[]
        for val in range(inp1,inp2):
                if(val>1):
                        for val1 in range(2,(val/2)+1):
                                if (val%val1==0):
                                        break
                        else:
                                l.append(val)
        return l
inp1=input("Enter the starting number :")
inp2=input("Enter the ending number :")
def prime_tuple(inp1=50,inp2=200):
        l=[]
        for val in range(inp1,inp2):
                if(val>1):
                        for val1 in range(2,(val/2)+1):
                                if (val%val1==0):
                                        break
                        else:
                                l.append(val)
        return tuple(l)

inp1=input("Enter the starting number :")
inp2=input("Enter the ending number : ")

if __name__ == "__main__":
	prime_num(inp)
	print prime_list(inp1,inp2)
	print prime_tuple(inp1,inp2)
	print "If no argumets passed then it wille take 1 ro 100:",prime_list()	
	print "If no argumets passedf through user it will take 50 to 200: ",prime_tuple()
