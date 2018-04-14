import string
import random

abcStr = string.ascii_lowercase + ' '
objStr = 'methinks it is like a weasel'
'''
def creat_string():
	global i_list
	global cha_list
	myStr = ''
	for i in range(len(objStr)):
		myStr += random.choice(abcStr)
#	print(myStr)
	return myStr
'''
def creat_string():
	global i_list
	global cha_list
	myStr = ''.join( random.choice(abcStr) for i in range(len(objStr)) )
#	print(myStr)
	return myStr
	
def compare_string(myStr):
	k = 0
	global i_list
	global cha_list
	for i in range(len(objStr)):
		if myStr[i] == objStr[i]:
			k += 1
#	k += 1 for i in range(len(objStr)) if myStr[i] == objStr[i]
#	print(k)
	return k

def find_correct():
	k_max = 0
	for i in range(1000):
		myStr = creat_string()
		k = compare_string(myStr)
		if k >= k_max:
			k_max = k
			myStr_max = myStr
		if k == len(objStr):
			print('find the correct string')
			print(myStr)
			return 1

	print(k_max)
	print(myStr_max)
	print(objStr)
	return 0


while True:
	if find_correct()==1:
		break
	
