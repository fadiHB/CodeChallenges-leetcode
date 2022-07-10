# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        res = list()

        def _walk(root):
            
            if root.left:
                _walk(root.left)
                
            res.append(root.val)
            
            if root.right:
                _walk(root.right)
                
        _walk(root)
        
        return res
        
        