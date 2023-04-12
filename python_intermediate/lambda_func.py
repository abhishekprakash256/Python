"""
also without iterations
the function to make the return at the iteration 
"""

#lambda arguments : expression 

#make a fuction

add_num = lambda x,y: x + y

a = [1,2,3,4,5]
b = map(lambda x: x*2,a)

print(list(b))