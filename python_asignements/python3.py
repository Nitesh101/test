"""
def comman_ele(list1,list2):
	return list(set(list1)&set(list2))
print(comman_ele([1,2,3,4],[2,4,5,6,7]))

def common_ele(list1,list2):
	for ele in list1:
		if ele in list2:
			print ele
	return
common_ele([1,2,3,4,6,7,8],[2,3,4,5,6,8,9])


def val(start=1,stop=100):
	#start = 1
	#stop = 100
	for num in range(start,stop+1):
		if num > 1:
			for i in range(2,num):
				if num%i == 0:
					#print num,"is not prime numbers"
					break
			else:
				print num,"prime numbers"

val(start=1,stop=40)
val(start=20)
val(stop=50)

mylist = [1, -1, 3, 2, -7, -5, 11, 6 ]
mylist = [-5, 7, -3, -4, 9, 10, -1, 11]
op=[]
index=0
for val in mylist:
	if val > 0:
		op.insert(index,val)
		index+=1
	else:
		op.append(val)
print op

def receive_list(lis):
	for val in lis:
		print  val*4,
	return 
receive_list([1,2,3,4])


def receive_list(lis):
	dict={}
	for val in lis:
		dict[val] = val*4
	return dict.values()
print(receive_list([1,2,3,4]))
"""
lst=[2,5,4,6,7]
num = 6
def func_1(lst, num):
    op=[]
    for val in lst:
        op.append(val*num)
    return op
print func_1(lst,num)
"""
def func_2(lst, num):
    for index in range(len(lst)):
        lst[index] = lst[index]*num
    return lst
    
print func_2(lst, num) 
"""
