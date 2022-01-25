'''
implement the concept of the binary_search in the list to search for an elememt, less number of the turns

'''
#make test cases 
lst_0 = [1,2,3,4,5,6,7,8,9,10,11]  #the element is present , odd lenth list
element_0 = 2 #passed

lst_1 = [1,2,3,5,6,7,8,9,12] #elememt not present 
element_1 = 0 #passed


lst_2 = [1,2,3,5,6,7,8,9,12] #last element 
element_2 = 12 # passed


lst_3 = [1,2,3,5,6,7,8,9,12] #first element
element_3 = 1 #passed


lst_4 = [1,2,3,5,6,6,6,6,6,7,8,9,11] #another element repetative
element_4 = 9 # passed

lst_5 = [1,2,3,5,6,6,6,6,7,8,9,11] #repetative element
element_5 = 6 #passed

lst_6 = [1,2,3,4,5,6,7,8,9,10]  #the element is present , even length of the list
element_6 = 3 #passed
 


#the main function

def binary_search(lst: list , query: int) -> int:
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

	step = 0 
	
	#initalize the pointers

	len_of_lst = len(lst)
	
	left = 0 

	right = len_of_lst - 1

	#start the loop 

	while left <= right:

		#find the mid 

		mid = (left + right)//2
		step+=1

		#check if mid element is equal , then return 
		if lst[mid] == query:
			return step, lst[mid]

		#if greater then , go right side
		elif lst[mid] < query:
			left = mid+1 

		#if less then , go left side
		elif lst[mid] > query:
			right = mid -1


	#return None if match not found

	return None

print(binary_search(lst = lst_0 , query = element_0))