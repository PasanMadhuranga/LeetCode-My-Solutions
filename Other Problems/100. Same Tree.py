# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if ((not p) and (not q)):
            return True
        
        if ((not p) or (not q) or p.val != q.val):
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    

# Another solution found in the discussion section. This is short but slower than the above solution.
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and q):
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
    
# The last return statement, return p is q, handles the cases where either p or q or both are None.
# This line checks:
# If both p and q are None, then it returns True (both are empty and trivially identical).
# If one of them is None but not the other, it returns False (one tree has more nodes than the other).