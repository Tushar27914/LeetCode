# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s=[]
        if root is None:
            return 0
        q=deque()
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
        s.sort()
        return s[k-1]
       # print(s)
        