'''
The question is to print the nth fibbonachi numbers as given input

numbers are - 0,1,1,2,3,5,8,13,21,34

			  1,2,3,4,5,6,7,8,9,10
'''

def fibbo_fun(n):

	last_two = [0,1]

	counter = 3

	while counter <= n :
		sum = last_two[0] + last_two[1]
		last_two[0] = last_two[1]

		last_two[1] = sum

		counter+=1

	return last_two[1]

print(fibbo_fun(5))