# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        # Helper function
        def isLeaf(root):
            if root is None:
                return False
            
            if root.left is None and root.right is None:
                return True
            
            return False
        
        # Initialize the total
        total = 0

        # Update result if root is not None
        if root is not None:

            # If left of root is None, then add the value of left child
            if isLeaf(root.left):
                total += root.left.val
            else:
                # Else recur for left child of root
                total += self.sumOfLeftLeaves(root.left)

            # Recur for right child of root and update total
            total += self.sumOfLeftLeaves(root.right)
            
        return total
    