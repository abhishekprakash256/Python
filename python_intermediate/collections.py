"""
The program to work on the collections of the python 
"""

#imports 

#the colections provide the data types like oredered dict 
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import deque  #can be appended on the left and the right side 


test = "aabdbsjcvttvv"

my_counter = Counter(test)


print(my_counter.items())

print(my_counter.values())

print(my_counter)


Point = namedtuple('Point','x,y')
pt = Point(1,-4)

print(pt.x,pt.y)

ordered_dict = OrderedDict()

ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5

print(ordered_dict)

que = deque()

que.append(1)
que.append(2)

que.appendleft(3)

print(que)