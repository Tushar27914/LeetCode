# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root is None):
            return []
        q=deque()
        q.append(root)
        res=[]
        while(len(q)):
            lev=[]
            for i in range(len(q)):
                ce=q.popleft()
                lev.append(ce.val)
                if(ce.left is not None):
                    q.append(ce.left)
                if(ce.right is not None):
                    q.append(ce.right)
            res.append(lev)
        return res    
        
        
        
# from collections import deque
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#         q = deque()
#         q.append(root)
#         res = []
#         while len(q):
#             lev = []
#             for i in range(len(q)):
#                 el = q.popleft()
#                 lev.append(el.val)
#                 if el.left:
#                     q.append(el.left)
#                 if el.right:
#                     q.append(el.right)
#             res.append(lev)      
#         return res