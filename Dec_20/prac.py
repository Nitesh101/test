def emp_data(em_data):
	fp = open('employee.txt','r')
	fa = fp.readlines()
	for name in fa:
		list1 = name.split(':')
		if list1[0] == em_data:
			print list1[0],':',list1[1]
def main():
	name = raw_input('enter a name: ')
	emp_data(name)
main()
