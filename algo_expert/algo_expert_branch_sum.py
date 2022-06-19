''' Algo for the sum calcultaion of sum in the BST 
Algo---------------
recursion approach in the binary tree
first check for the root node if null return (base case)
sun = 0
then check child either null or not left.value == none or right.value == none
call the function
as per child call the sum 
function(root)
'''
def function_1(root):        #first function 
	sum_lst= []              #lst for the sum collection
	function_2(root,0,sum_lst)      #fuction call
	return sum_lst                              #return of the lst of sums

def function_2(node,running_sum,sum_lst):   #the recursion function
	if node is None:
		return 0

	new_running_sum = running_sum + node
	

	if node.left is None and node.right is None:       #base case for the end of recursion
		sum_lst.append(new_running_sum)
		return 

	function_2(root.left, new_running_sum, sum_lst)         #recursion calling
	function_2(root.right,new_running_sum, sum_lst)	        #recursion calling 

                 


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = int(data)

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = int(Node(data))
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = int(Node(data))
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()



root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

print(function_1(root))

root.PrintTree()







