'''
The question is to print the nth fibbonachi numbers as given input

numbers are - 0,1,1,2,3,5,8,13,21,34

			  1,2,3,4,5,6,7,8,9,10
'''

def fibbo_fun(n , memoize = {1: 0 , 2 : 1}):

	if n in memoize:

		return memoize[n]

	else:

		memoize[n] = fibbo_fun(n-1, memoize) + fibbo_fun(n-2 , memoize)
		return memoize[n]


print(fibbo_fun(5))	