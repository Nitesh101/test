data_list = [1,10,5,15,13]
#print sorted(data_list)
#print sorted(data_list, reverse=True)
new_list = []
while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
   	data_list.remove(minimum)    

print new_list
