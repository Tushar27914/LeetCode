# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 
        t=root.left.val
        u=root.right.val
        w=root.val
        if(t+u==w):
            return True
        return False