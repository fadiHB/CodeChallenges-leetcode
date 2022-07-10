# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isSymmetric(root1, root2):
            # Both of them are None
            if (root1 is None) and (root2 is None): return True
            
            # Both of them are not None
            if (root1 is not None) and (root2 is not None):
                if root1.val == root2.val:
                    return isSymmetric(root1.left, root2.right) and isSymmetric(root1.right, root2.left)
                
            # Else for the above two nested-condition both:
                # if (root1 is not None) and (root2 is not None) == False # So one of them is None.
                # if  root1.val != root2.val # so they are not equal
                # return False
                
            return False
                
        return isSymmetric(root.left, root.right)
            
        