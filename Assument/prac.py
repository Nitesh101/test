def frequence(lst):
	output = [[], []]
	min_freq = min(lst, key=lst.count)
	output[0].append(min_freq)
	max_freq = max(lst, key=lst.count)
	output[1].append(max_freq)
	for val in lst:
		if val not in output[0] and val not in output[1]:
			if lst.count(min_freq) == lst.count(val):
				output[0].append(val)
			elif lst.count(max_freq) == lst.count(val):
				output[1].append(val)
	return output
lst1 = [13, 12, 11, 13, 14, 13, 7, 11, 13, 14, 12, 14, 14]
if __name__ == "__main__":
	print (frequence(lst1))
