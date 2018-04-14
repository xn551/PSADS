class Fraction:
	def __init__(self, top, bottom):
		if not isinstance(top,int) or not isinstance(bottom,int):
			raise RuntimeError("top or bottom should be integer")
		else:
			common = gcd2(top, bottom)
			self.num = top//common
			self.den = bottom//common
	def show(self):
		print(str(self.num)+ "/"+ str(self.den))
	def __str__(self):
		return (str(self.num)+ "/"+ str(self.den))
	def __add__(self,other):
		new_num = self.num*other.den + other.num*self.den
		new_den = self.den * other.den
		return Fraction(new_num, new_den)
	def __sub__(self,other):
		new_num = self.num*other.den - other.num*self.den
		new_den = self.den * other.den
		if new_num == 0:
			return 0
		else:
			return Fraction(new_num, new_den)
	def __mul__(self, other):
		new_num = self.num*other.num
		new_den = self.den * other.den
		return Fraction(new_num, new_den)
	def __div__(self, other):
		new_num = self.num * other.den
		new_den = self.den * other.num
		return Fraction(new_num, new_den)
	def __eq__(self, other):
		first_num = self.num * other.den
		second_num = self.den * other.num
		return first_num == second_num
	
	def __lt__(self, other):
		first_num = self.num * other.den
		second_num = self.den * other.num
		return first_num < second_num
	
	def __gt__(self, other):
		first_num = self.num * other.den
		second_num = self.den * other.num
		return first_num > second_num

	def get_num(self):
		return self.num

	def get_den(self):
		return self.den

def gcd(m,n):
	while m%n != 0:
		old_m = m
		old_n = n

		m = old_n
		n = old_m % old_n
	return n

def gcd2(m,n):
	r = m%n
#	print("r",r)
	if r == 0:
#		print("n",n)
		return n
	else:
		return gcd2(n,r)




if __name__ == '__main__':
	my_f = Fraction(1,2)
	my_f.show()
	print('I ate' , my_f)
	my_f2 = Fraction(3,6)
	print(my_f + my_f2)
	print(gcd(100,5))
	print(my_f == my_f2)
	print(my_f - my_f2)
	print(my_f * my_f2)
	print(my_f > Fraction(1,4))
	print(my_f < Fraction(1,4))
	print(my_f.get_num())
	print(my_f.get_den())
