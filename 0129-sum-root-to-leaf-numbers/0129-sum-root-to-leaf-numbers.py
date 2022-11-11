# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root,pathsum):
            if root is None:
                return 0
            pathsum=pathsum*10+root.val
            if root.left is None and root.right is None:
                return pathsum
            return dfs(root.left,pathsum) + dfs(root.right,pathsum)
        return dfs(root,0)
        
        
        
        
