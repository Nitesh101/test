#!/usr/bin/python
def count(x):
    zeros = 0                     
    for i in range (2,x+1): 
        print(i)
        if x > 0:
            if i % 5 == 0:       
                print("count")    
                zeros +=1       
        else:
            ("False")
    print(zeros)        

count(6)
