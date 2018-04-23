import timeit
from timeit import Timer
import random

for i in range(100000, 1000001, 100000):
	#index_list = Timer("x.index(random.randrange(%d))" %i, "from __main__ import random, x")
	#index_list = Timer("x.index(1000)" , "from __main__ import x")
	index_list = Timer("x.index(random.randrange(1000))" , "from __main__ import random, x")
	x = list(range(i))
	pt = index_list.timeit(number=50)
	print("%15.5f" %pt)
