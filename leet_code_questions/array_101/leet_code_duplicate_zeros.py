"""
to make the array that have the duplicate zeros in the output 
and shift the places of the other elements
"""

Input = [1,0,2,3,0,4,5,0]
Output =[1,0,0,2,3,0,0,4]

Input2= [1,2,3]
Output2 = [1,2,3]

Input3 = [1,0,2,3,0,4,5,0]
output3 = [1,0,0,2,3,0,0,4]


"""
the length of the array is imp 
shifting the position is imp 
"""

class Solution:
    def duplicateZeros(self, arr:int) -> None:
        """
        Do not return anything, modify arr in-place instead.
        Args:
        	arr (list): the interger of the array
        Return:
        	modified_lst (list) : the modified array of the integer 
        """

        length_arr = len(arr) - 1
        i = 0
        modified_arr = []

        while i < length_arr - 1:
        	# the iterator

        	if arr[i] == 0:
        		modified_arr.append(arr[i])
        		modified_arr.append(0)
        	else:
        		modified_arr.append(arr[i])
        	i+=1
        return modified_arr


if __name__ == '__main__':
	soln = Solution()
	res = soln.duplicateZeros(Input3)
	print(res)
