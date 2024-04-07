# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.DFStraverse(root.left, root.right, 1)
        return root
    
    def DFStraverse(self, subtree1, subtree2, level):
        if (subtree1 == None): return

        if (level % 2):
            subtree1.val, subtree2.val = subtree2.val, subtree1.val
        

        self.DFStraverse(subtree1.left, subtree2.right, level + 1)
        self.DFStraverse(subtree1.right, subtree2.left, level + 1)


# Another faster solution found online
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def flipOdd(lnode, rnode, level):
            if not lnode and not rnode:
                return
            if level % 2 == 1:
                    lnode.val, rnode.val = rnode.val, lnode.val
            flipOdd(lnode.left, rnode.right, level + 1)
            flipOdd(lnode.right, rnode.left, level + 1)
        
        flipOdd(root.left, root.right, 1)
        return root
        