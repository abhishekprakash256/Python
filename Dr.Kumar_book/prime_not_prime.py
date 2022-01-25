"""
The function checks for the prime number and takes input from the user to check 
Question 13 , Chapter 1

"""

def prime_checker(num:int)-> bool:

	count = 0

	for i in range(1,num+1):

		if num %i == 0:
			count +=1

			if count >2 : 

				return True

	return False


def check_prime(num:int)-> str:
	"""
	The function takes the user input and check if a number is prime or not 

	Arguments:

		num (int) -> the number checks whether it is prime or not

	Return:

		message (string) -> the number is prime or not 


	"""

	

	while True :

		num = int(input("Enter to check the number is prime or not : "))

		if num == 0:

			break

		elif num == 1:

			print("The number is not prime") 

		elif prime_checker(num) == False:

			print("The number is prime")

		elif prime_checker(num) == True:

			print("The number is not prime")

	return "Done"




print(check_prime(1))