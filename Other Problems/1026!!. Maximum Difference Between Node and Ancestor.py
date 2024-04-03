# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.recmaxAncDiff(root, root.val, root.val)
    

    def recmaxAncDiff(self, root, curMax, curMin):
        if (not root): return 0

        curMax = max(root.val, curMax)
        curMin = min(root.val, curMin)

        LsubMaxDiff = self.recmaxAncDiff(root.left, curMax, curMin)
        RsubMaxDiff = self.recmaxAncDiff(root.right, curMax, curMin)

        return max(curMax - curMin, LsubMaxDiff, RsubMaxDiff)
        

# Anotther solution found in the discussion section
class Solution:
    def maxAncestorDiff(self, root, mn=100000, mx=0):
        return max(self.maxAncestorDiff(root.left, min(mn, root.val), max(mx, root.val)), \
            self.maxAncestorDiff(root.right, min(mn, root.val), max(mx, root.val))) \
            if root else mx - mn
        