# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sortedList = []
        def getSortedList(node):
            if node is None:
                return
            getSortedList(node.left)
            sortedList.append(node.val)
            getSortedList(node.right)
        
        getSortedList(root)

        return self.createBalancedBST(sortedList)

    def createBalancedBST(self, sortedList):
        if (not sortedList): return None

        n = len(sortedList)
        mid = n//2
        root = TreeNode(sortedList[mid])

        root.left = self.createBalancedBST(sortedList[:mid])
        root.right = self.createBalancedBST(sortedList[mid+1:])

        return root
    
# You can use Day-Stout-Warren (DSW) algorithm to balance given Binary Search Tree
import math

# Function to convert input BST to right linked list known as vine or backbone.
def bstToVine(grand: TreeNode) -> int:
	count = 0

	# Make tmp pointer to traverse and right flatten the given BST
	tmp = grand.right

	# while tmp is not null
	while tmp:

		# If left exist for node pointed by tmp then right rotate it
		if tmp.left:
			oldTmp = tmp
			tmp = tmp.left
			oldTmp.left = tmp.right
			tmp.right = oldTmp
			grand.right = tmp

		# If left dont exists add 1 to count and traverse further right to flatten remaining BST
		else:
			count += 1
			grand = tmp
			tmp = tmp.right

	return count

# Function to compress given tree with its root as grand.right
def compress(grand: TreeNode, m: int) -> None:

	# Make tmp pointer to traverse and compress the given BST
	tmp = grand.right

	# Traverse and left-rotate root m times to compress given vine form of BST
	for i in range(m):
		oldTmp = tmp
		tmp = tmp.right
		grand.right = tmp
		oldTmp.right = tmp.left
		tmp.left = oldTmp
		grand = tmp
		tmp = tmp.right

# Function to implement the algorithm
def balanceBST(root: TreeNode) -> TreeNode:

	# create dummy node with value 0
	grand = TreeNode(0)

	# assign the right of dummy node as our input BST
	grand.right = root

	# get the number of nodes in input BST and simultaneously convert it into right linked list.
	count = bstToVine(grand)

	# get the height of tree in which all levels are completely filled
	h = int(math.log2(count + 1))

	# get number of nodes until second last level
	m = pow(2, h) - 1

	# left rotate for excess nodes at last level
	compress(grand, count - m)

	# left rotate till m becomes 0
	# Steps is done as mentioned in algorithm to make BST balanced.
	for m in [m // 2**i for i in range(1, h + 1)]:
		compress(grand, m)

	# return the root of the balanced binary search tree
	return grand.right

# Function to print preorder traversal of Binary tree
def preorderTraversal(root: TreeNode) -> None:
	if not root:
		return
	print(root.val, end=" ")
	preorderTraversal(root.left)
	preorderTraversal(root.right)
	return

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
	    return balanceBST(root)

        