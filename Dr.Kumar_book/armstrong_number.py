"""
The function and print armstrong number in that interval

"""


def check_armstrong(number:int)-> bool:

	number = str(number)

	length_num = len(number)

	sum_num = 0

	for j in range(length_num):

		indiv_cube = int(number[j]) * int(number[j]) * int(number[j])

		sum_num += indiv_cube

	if sum_num == int(number):

		return True

	else:

		return False 





def print_armstrong()-> int:
	"""
	The function takes two numbers and print the armstrong number between them

	Arguments:
		num_1 , num_2 (int) -> the two number between whose we check the armstronmg number

	Return:

		nums (int) , the armstrong numbers


	"""

	while True:

		num_1 = int(input("Enter the number 1 : "))

		num_2 = int(input("Enter the number 2 : "))

		if num_2 == 0:

			break

		else:

			for i in range(num_1, num_2+1):

				if check_armstrong(i) == True:

					print(i)

	return "Done"


print(print_armstrong())
