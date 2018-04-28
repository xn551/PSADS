from Stack import Stack

def par_checker(symbol_string):
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbol_string) and balanced:
		symbol = symbol_string[index]
		if symbol in "([{)]}":
			if symbol in "([{":
				s.push(symbol)
			elif s.is_empty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top, symbol):
					balanced = False
		index = index + 1

	if balanced and s.is_empty():
		return True
	else:
		return False

def matches(Open, Close):
	opens = "([{"
	closes = ")]}"
	return opens.index(Open) == closes.index(Close)

if __name__ == "__main__":
	print(par_checker('{{(([]))}}'))
