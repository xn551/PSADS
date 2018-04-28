from Stack import Stack

def par_checker(symbol_string):
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbol_string) and balanced:
		symbol = symbol_string[index]
		if symbol in "()":
			if symbol == "(":
				s.push(symbol)
			elif s.is_empty():
				balanced = False
			else :
				s.pop()
		index = index + 1

	if balanced and s.is_empty():
		return True
	else:
		return False

if __name__ == "__main__":
	print(par_checker('(1+3)*(2+4*6)'))
	print(__name__)
