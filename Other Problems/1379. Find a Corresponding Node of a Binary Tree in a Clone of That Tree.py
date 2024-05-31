# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [cloned]

        while(len(stack) > 0):

            if (stack[0].val == target.val):
                return stack[0]
            node = stack.pop(0)

            if node.left is not None:
                stack.append(node.left)

            if node.right is not None:
                stack.append(node.right)
            