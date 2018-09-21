row_num = int(input("input number of rows: "))
col_num = int(input("input number of columns: "))
multi_list = []
for row in range(row_num):
	for col in range(col_num):
		multi_list.append(row*col)
print multi_list
