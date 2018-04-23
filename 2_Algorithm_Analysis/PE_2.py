import timeit
from timeit import Timer
import random

for i in range(100000, 1000001, 100000):
	get_dict = Timer("x.get(random.randrange(%d))" %i , "from __main__ import random, x")
	set_dict = Timer("x[random.randrange(%d)]= 1" %i, "from __main__ import random, x")
	x = { j:None for j in range(i)}

	pget = get_dict.timeit(number=50)
	pset = set_dict.timeit(number = 50)
	print("%d, %15.5f, %15.5f" %(i, pget, pset))
