#the iterative approach for fidning the closest value in the BST
# Average time - O(Log(n)) | worst-  O(n))
# Space O(log(n)) | worst O((n))



def findClosestValueInBst(tree, target):
	return findClosestValueInBstHelper(tree, target, float("infinity"))


def findClosestValueInBstHelper(tree, target, closest):
	if tree is None:
		return closest
	elif abs( target - closest) > abs(target - tree.value):
		closest = tree.value
	elif target < tree.value :
		return findClosestValueInBstHelper(tree.left, target, closest)
	elif target > tree.closest:
		return findClosestValueInBstHelper(tree.right, traget, closest)
	else:
		return closest		



#-----------------------------------the iertrative approah-------------------------------------------------------	


def findClosestValueInBst(tree, target):
	return findClosestValueInBstHelper(tree, target, float("infinity"))


def findClosestValueInBstHelper(tree, target, closest):
	currentNode = tree
	while currentNode is not None:
		if abs(target - closest) > abs(target - currentNode.value):
			closest = currentNode.value
		elif abs( target - closest) > abs(target - currentNode.value):
			closest = currentNode.value
		elif target < currentNode.value :
			currentNode = currentNode.left
		elif target > currentNode.closest:
			currentNode = currentNode.right
		else:
			break

	return closest 



