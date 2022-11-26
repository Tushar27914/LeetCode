# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        ans=TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))
        ans.left = self.mergeTrees(root1 and root1.left, root2 and root2.left)
        ans.right = self.mergeTrees(root1 and root1.right , root2 and root2.right)
        return ans
        
        
        
        
        
        
        
        
        
        
        
#         def mergeTrees(self, t1, t2):
#     if not t1 and not t2: return None
#     ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
#     ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
#     ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
#     return ans