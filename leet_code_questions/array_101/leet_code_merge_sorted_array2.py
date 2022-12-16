"""
given the two sorted array merge with the number given
the inputs are two lists and m and n the number of the integer to be merged 

"""

"""
class Solution:
	def merge_array(self,lst1: list , m : int , lst2 : list, n: int ):
		
		The function takes the two sorted array and gives a combined array of sorted elements
		Args:
			lst1: (list) The sorted list
			m : (int) The number of elements
			lst2: (list) The sorted list
			n : (int) The number of elements
		Return:
			combined_arr: (list) the combined sorted array 
		
		i = 0 
		j = 0 
		combined_list = []

		while (i != m and j != n):
			if lst1[i] > lst2[j]:
				combined_list.append(lst2[j])
				if j == m:
					j=j
				else:
					j+=1
			elif lst1[i] == lst2[j]:
				combined_list.append(lst1[i])
				j+=1
				i+=1
			else:
				combined_list.append(lst1[i])
				if i == n:
					i=i
				else:
					i+=1

		return combined_list


class Solution:
	def merge_array(self,lst1: list, m : int, lst2 : list , n : int):
		
		The function takes the two array and gives the combined array of the two input
		Args:
			lst1: (list) The list of the sorted integers
			m : (int) The number of the non zero elements 
			lst2 : (list) The list of the sorted intergers 
			n : (int) The number of the non zero elements  
		
		i = 0 
		j = 0 
		combined_lst = []

		while (i < m and j < n):
			
			if lst1[i] < lst2[j]:
				combined_lst.append(lst1[i])
				if i == m:
					i+=0
				else:
					i +=1
			elif lst1[i] == lst2[j]:
				combined_lst.append(lst1[i])
				i+=1
				j+=1
			else:
				combined_lst.append(lst2[j])
				if j == n:
					j +=0
				else:
					j+=1

		return combined_lst


if __name__ == '__main__':
	sol = Solution()
	res = sol.merge_array(nums1,m,nums2,n)
	print(res)

"""


nums1 = [1,2,3,0,0,0]
m = 3 
nums2 = [2,5,6] 
n = 3
out1 = [1,2,2,3,5,6]


nums3 = [1]
m1 = 1 
nums4 = []
n1 = 0
out2 = [1]


class Solution:
	def merge(self,list1,m,list2,n):
		
		i = 0
		j = 0 
		combined_array = []

		while(i+j) < (m+n):

			if (list1[i] < list2[j]) and list1[i] !=0 and list2[j] !=0:
				combined_array.append(list1[i])
				if i == m:
					i+=0
					combined_array.append(list2[j])
					j+=1
				else:
					i+=1
			elif (list1[i] == list2[j]) and list1[i] !=0 and list2[j] !=0:
				combined_array.append(list1[i])
				combined_array.append(list2[j])
				i+=1
				j+=1
			else:
				if list1[i] !=0 and list2[j] !=0:
					combined_array.append(list2[j])
					if j == n:
						j+=0
						combined_array.append(list1[i])
						i+=1
					else:
						j+=1
				else:
					pass


		return combined_array

if __name__ == '__main__':
	sol = Solution()
	res = sol.merge(nums1,m,nums2,n)
	print(res)
