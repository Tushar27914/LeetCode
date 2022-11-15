# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        s=[]
        if root is None:
            return 0
        q=deque()
        q.append(root)
        q.append(root)
        while len(q)!=0:
            level_size=len(q)
            for i in range(level_size):
                ce=q.popleft()
                s.append(ce.val)
                if ce.left is not None:
                    q.append(ce.left)
                if ce.right is not None:
                    q.append(ce.right)
        s=list(set(s))
        if len(s)==1:
            return -1
        s.sort()
        return s[1]
            
        