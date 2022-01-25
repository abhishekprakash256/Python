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

	#find the length of the list, or remaing list , 

		len_of_lst = len(lst)

		#check for odd and even length , find the middle element 

		if len_of_lst % 2 == 0 :

			#middle element
			mid_element_0 = len_of_lst/2 - 1
	
			steps +=1
			#found then return 
			mid_element_0 = int(mid_element_0)
			if query == lst[mid_element_0]:
				return lst[mid_element_0] , steps
			elif query > lst[mid_element_0]:
				mid_element_0 = int(mid_element_0)
				lst = lst[mid_element_0: len_of_lst]
			elif query < lst[mid_element_0] :
				mid_element_0 = int(mid_element_0)
				lst = lst[0:mid_element_0]
			#not found exit by returning -1  
			else:
				return - 1


		else :


			mid_element_0 = len_of_lst/2
			mid_element_1 = len_of_lst/2 + 1 
			steps +=1
			#found then return 
			mid_element_0 = int(mid_element_0)
			mid_element_1 = int(mid_element_1)
			if query == lst[mid_element_0]:
				return lst[mid_element_0], steps
			elif query == lst[mid_element_1]:
				mid_element_1 = int(mid_element_1)
				return lst[mid_element_1], steps
			elif query >= lst[mid_element_0] :
				mid_element_0 = int(mid_element_0)
				lst  = lst[mid_element_0:len_of_lst]
			elif query <= lst[mid_element_1]:
				mid_element_1 = int(mid_element_1)
				lst = lst[0:mid_element_1]
			#not found exit by returning -1 
			else:
				return -1 


print(search(lst = lst_0, query = element_0))






	


