# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
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
        t=[]
        for i in range(len(s)):
            if s[i]>=low and s[i]<=high:
                t.append(s[i])
        return sum(t)
        