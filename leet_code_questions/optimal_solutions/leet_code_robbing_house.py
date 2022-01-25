#the robbing problem to rob the house one after the other 
# we can't rob the consecutive houses

lst = input("Enter the lst of houses: - ")

lst = list(lst)

lst_2 = []

for i in lst:
	lst_2.append(int(i))

print(lst_2)

class Solution:	
	def __init__(self,x):
		self.x = x
	def rob_house(self):
		rob_1,rob_2 = 0,0
		for n in self.x:
			temp = max(n + rob_1, rob_2)
			rob_1 = rob_2
			rob_2 = temp
		return temp




ins = Solution(lst_2)


print(ins.rob_house())
