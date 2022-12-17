"""
using the inbuild python stack as the list

"""

stack0 = []


#push operation
stack0.append('a')
stack0.append('b')
stack0.append('c')

#after the push operation
print(stack0)

#pop operation 
stack0.pop()


#after the pop operation
print(stack0)



#impelemtation using the collections 

from collections import deque

stack1 = deque()

#push the eleements
stack1.append(1)
stack1.append(2)
stack1.append(3)

#pop the elements in the queue
stack1.pop()
stack1.pop()

#print after the pop
print(stack1)