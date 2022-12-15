"""
given the two sorted array merge with the number given
the inputs are two lists and m and n the number of the integer to be merged 

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
	def merge_array(self,lst1: list , m : int , lst2 : list, n: int ):
		"""
		The function takes the two sorted array and gives a combined array of sorted elements
		Args:
			lst1: (list) The sorted list
			m : (int) The number of elements
			lst2: (list) The sorted list
			n : (int) The number of elements
		Return:
			combined_arr: (list) the combined sorted array 
		"""
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


if __name__ == '__main__':
	sol = Solution()
	res = sol.merge_array(nums1,m,nums2,n)
	print(res)