def My_reverse(aString):
	string_list = []
	reverse_string = []
	for i in range(len(aString)):
		string_list.append(aString[i])
	while not string_list == []:
		reverse_string.append(string_list.pop())
	return ''.join(reverse_string)

print( My_reverse("abcdefghijk") )
