'''
word_list = ['cat','dog','rabbit']
letter_list = []
for a_word in word_list:
	for a_letter in a_word:
		letter_list.append(a_letter)
		if letter_list.count(a_letter) > 1:
			letter_list.remove(a_letter)
print(letter_list)
'''
'''
word_list = ['cat','dog','rabbit']
letter_list = []
for a_word in word_list:
	for a_letter in a_word:
		if letter_list.count(a_letter) == 0:
			letter_list.append(a_letter)

print(letter_list)
'''
'''
word_list = ['cat','dog','rabbit']
letter_list = []
for a_word in word_list:
	for a_letter in a_word:
		if a_letter in letter_list:
			continue
		letter_list.append(a_letter)

print(letter_list)
'''
'''
word_list = ['cat','dog','rabbit']
letter_list = []
for a_word in word_list:
	for a_letter in a_word:
		if a_letter not in letter_list:
			letter_list.append(a_letter)

print(letter_list)
'''
word_list = ['cat','dog','rabbit']
letter_list = []
for a_word in word_list:
	letter_list += [a_letter for a_letter in a_word if a_letter not in letter_list]

print(letter_list)
