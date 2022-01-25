'''
To find the median of the two array by merging and the sorted 

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Input: nums1 = [], nums2 = [1]
Output: 1.00000

Input: nums1 = [2], nums2 = []
Output: 2.00000
'''

nums1 = str(input("Enter the aaray 1: "))
nums2 = str(input("Enter the array 2: "))

def the_median(nums1,nums2):
	lst_1=[]
	lst_2=[]
	for i in  nums1:
		lst_1.append(int(i))
	for i in nums2:
		lst_2.append(int(i))	
	lst_3 = lst_1 + lst_2
	lst_3.sort()
	if (len(lst_3)%2) == 0:
		return  float((lst_3[int((len(lst_3)/2)-1)] + lst_3[int((len(lst_3)/2))])/ 2)
	else:
		return float(lst_3[int((len(lst_3)+1)/2)-1])		

print(the_median(nums1,nums2))

