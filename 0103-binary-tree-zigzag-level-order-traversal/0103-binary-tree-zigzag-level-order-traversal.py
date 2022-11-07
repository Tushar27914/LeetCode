# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import *
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans,q,c=[],[root],1
        while q:
            n,l=len(q),[]
            for i in range(n):
                ce=q.pop(0)
                l.append(ce.val)
                if(ce.left):
                    q.append(ce.left)
                if(ce.right):
                    q.append(ce.right)
            if c==1:
                ans.append(l)
            else:
                ans.append(l[::-1])
            c=1-c
        return ans
        
        # if not root: return []
        # ans,q,c = [],[root],1
        # while q:
        #     n,l = len(q),[]
        #     for i in range(n):
        #         curr = q.pop(0)
        #         l.append(curr.val)
        #         if curr.left:
        #             q.append(curr.left)
        #         if curr.right:
        #             q.append(curr.right)
        #     if c == 1:
        #         ans.append(l)
        #     else:
        #         ans.append(l[::-1])
        #     c = 1-c
        # return ans

        
        