#!/usr/bin/python
def Emp_data(Emp_name):
	fp = open("employee.txt", 'r')
	emp_list = fp.readlines()
	for name in emp_list:
		list1 = name.split(":")
		if list1[0] == Emp_name:	
			print list1[0], ' : ', list1[1]
   	fp.close()
def main():
    name = raw_input("Enter Emp name: ")
    Emp_data(name)
main()


