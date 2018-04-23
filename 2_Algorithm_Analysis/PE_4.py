import random

def find_kmin(k,alist):
	for j in range(k):
		for i in range(len(alist)-1):
			if alist[i] < alist[i+1]:
				b = alist[i+1]
				alist[i+1] = alist[i]
				alist[i] = b
		lst_one = alist.pop()
		print(alist)
	return lst_one

aList = list(range(20))
random.shuffle(aList)
print(aList)
print(find_kmin(11,aList))
				
		
	
