class Fraction:
	def __init__(self, top, bottom):
		self.num = top
		self.den = bottom
	def show(self):
		print(str(self.num)+ "/"+ str(self.den))
	def __str__(self):
		return (str(self.num)+ "/"+ str(self.den))
	def __add__(self,other):
		new_num = self.num*other.den + other.num*self.den
		new_den = self.den * other.den
		common = gcd2(new_num, new_den)
		return Fraction(new_num//common, new_den//common)
	def __sub__(self,other):
		new_num = self.num*other.den - other.num*self.den
		new_den = self.den * other.den
		common = gcd2(new_num, new_den)
		if new_num == 0:
			return 0
		else:
			return Fraction(new_num//common, new_den//common)
	def __mul__(self, other):
		new_num = self.num*other.num
		new_den = self.den * other.den
		common = gcd2(new_num, new_den)
		return Fraction(new_num//common, new_den//common)
	def __div__(self, other):
		new_num = self.num * other.den
		new_den = self.den * other.num
		common = gcd2(new_num, new_den)
		return Fraction(new_num//common, new_den//common)
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
