# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0;

        # compute the depth of each subtree
        lDepth = self.maxDepth(root.left)
        rDepth = self.maxDepth(root.right)

        # use the larger one
        if (lDepth > rDepth):
            return (lDepth + 1)
        
        elif (rDepth > lDepth):
            return (rDepth + 1)
        
        elif (rDepth == lDepth):
            # here we can return rDepth+1 or lDepth+1 , No matter in this case
            return lDepth+1
        