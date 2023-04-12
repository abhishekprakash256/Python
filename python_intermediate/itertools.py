"""
usin the iter tools in the python
"""

from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import accumulate  # the accumulate can also take fucntions that are changed as per requirementr
import operator
from itertools import groupby


a = [1,2]
b = [3,4]
c = [1,2,3,4,5,6]


def smaller_than_3(x):
	return x < 3

prod = product(a,b)
permu = permutations(a)
comb = combinations(b,1)
accm = accumulate(c)
accm_func = accumulate(c,func=operator.mul )
group_obj = groupby(a,key = smaller_than_3)

for key,value in group_obj:
	print(key,list(value))


print(list(prod))
print(list(permu))
print(list(comb))
print(list(accm))

print(list(accm_func))