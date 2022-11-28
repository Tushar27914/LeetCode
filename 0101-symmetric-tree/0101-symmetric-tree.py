# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if(root is not None and root.left is None and root.right is None):
            return True
        if(root.left is not None and root.right is not None):
            return self.symmetric(root.left, root.right)
        
    def symmetric(self,a,b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.val==b.val and self.symmetric(a.left,b.right) and self.symmetric(a.right,b.left):
            return True
        else:
            return False
            
        