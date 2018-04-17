def Find_min_n2(a_list):
	for number in a_list:
		k = 0
		for other_number in a_list:
			if number <= other_number:
				k += 1
		if k == len(a_list):
			return number

def Find_min_n(a_list):
	for i in range(0,len(a_list)-1):
		if a_list[i] <= a_list[i+1]:
			b = a_list[i+1]
			a_list[i+1] = a_list[i]
			a_list[i] = b
	return a_list[len(a_list)-1]

print(Find_min_n2([1,-1,2,4,6,0,3]))
print(Find_min_n([1,-2,-3,4,6,8]))
