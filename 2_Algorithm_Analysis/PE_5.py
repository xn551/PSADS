import random

def find_kmin(k,alist):
	alist.sort()
	return alist[k-1]

aList = list(range(20))
random.shuffle(aList)
print(aList)
print(find_kmin(11,aList))
				
		
	
