"""
The program to print the fibbonache numbers

0,1,1,2,3,5,8,13,21 - fibbonachi numbers

1 2 3 4 5 6 7 8 9

Question 15, chapter 1
"""

def print_fibb():
	"""
	The function print the fibbonachi numbers for the user

	Return:

		nums (int) -> The fibbonachi numbers


	"""

	running_num = 0

	curr_num = 0

	while True:

		print(" ")

		number_of_fibbo = int(input("Enter the number of fibbonachi numbers you want : "))

		if number_of_fibbo == 0:

			break

		else:
			for i in range(1,number_of_fibbo+1):

				if i == 1:

					print(0, end =" ")

					running_num = 0

					prev_num_1 = running_num


				elif i == 2:

					print(1, end =" ")

					running_num = 1

					prev_num_2 = running_num
			

				else:

					curr_num = prev_num_1 + prev_num_2

					prev_num_1 = prev_num_2

					prev_num_2 = curr_num


					print(curr_num , end = " ")






print(print_fibb())











