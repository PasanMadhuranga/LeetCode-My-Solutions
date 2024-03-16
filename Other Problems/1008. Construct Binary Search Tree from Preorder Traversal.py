# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if (not preorder): return None

        n = len(preorder)
        root = TreeNode(preorder[0])
        for i in range(1, n):
            if (preorder[i] > preorder[0]):
                root.left = self.bstFromPreorder(preorder[1:i])
                root.right = self.bstFromPreorder(preorder[i:])
                break
        else:
            root.left = self.bstFromPreorder(preorder[1:])
        return root



# Another solution found in the discussion section
def bstFromPreorder(self, A):
    # Helper function to construct BST from preorder traversal
    # i: start index of the current segment of preorder traversal
    # j: end index of the current segment of preorder traversal
    def helper(i, j):
        # Base case: if the current segment is empty, return None
        if i == j: 
            return None
        
        # The first element in the segment is the root of the BST
        root = TreeNode(A[i])
        
        # Find the index where elements start being greater than A[i], which indicates
        # the division between left subtree and right subtree elements in the preorder array.
        # bisect.bisect is used to find the position to insert A[i] to keep the list sorted
        # and thus helps in identifying the start of right subtree.
        mid = bisect.bisect(A, A[i], i + 1, j)
        
        # Recursively construct the left subtree from the elements between
        # the current root and the mid-point.
        root.left = helper(i + 1, mid)
        
        # Recursively construct the right subtree from the elements between
        # the mid-point and the end of the current segment.
        root.right = helper(mid, j)
        
        # Return the root of the constructed subtree
        return root
    
    # Call the helper function with the entire range of the preorder array
    return helper(0, len(A))
