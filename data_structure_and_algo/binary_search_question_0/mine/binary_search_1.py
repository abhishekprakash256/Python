'''
implement the concept of the binary_search in the list to search for an elememt, less number of the turns

'''

#make test cases 
lst_0 = [1,2,3,4,5,6,7,8,9,10,11]  #the element is present , odd lenth list
element_0 = 2 #not passed

lst_1 = [1,2,3,5,6,7,8,9,12] #elememt not present 
element_1 = 0 #not passed


lst_2 = [1,2,3,5,6,7,8,9,12] #last element 
element_2 = 12 #passed


lst_3 = [1,2,3,5,6,7,8,9,12] #first element
element_3 = 1 #passed


lst_4 = [1,2,3,5,6,6,6,6,6,7,8,9,11] #another element repetative
element_4 = 9 #passed

lst_5 = [1,2,3,5,6,6,6,6,7,8,9,11] #repetative element
element_5 = 6 #passed

lst_6 = [1,2,3,4,5,6,7,8,9,10]  #the element is present , even length of the list
element_6 = 3 #passed
 


#the main function

def search(lst: list , query : int) -> int:
	'''
	The function takes the list and query, peform the search
	gives the number of steps taken to find

	Arguements:
		lst : sorted list of the elements
	---------------------------------------------
	Returns:
		turns : integer , number of turns taken to find the element
	'''

	#start the steps varibale

	steps = 0 

	#start a loop 

	for i in range(0,20):
		#getting the length
		length_of_lst = len(lst)
		steps +=1

		#legth of the list can be odd and even

		if length_of_lst % 2 == 0 :# even length list

		#check for element if matches then return 
			if query == lst[length_of_lst/2] :
				return query , steps
			#check if greater that middle element look right 
			elif query > lst[length_of_lst/2]:
				lst = lst[length_of_lst/2 : length_of_lst]
			#check if less than middle element look left
			elif query < lst[length_of_lst/2]:
				lst = lst[0:length_of_lst/2]


	#return None if not found
	return None 


print(search(lst = lst_0 , query = element_0))







	



	

