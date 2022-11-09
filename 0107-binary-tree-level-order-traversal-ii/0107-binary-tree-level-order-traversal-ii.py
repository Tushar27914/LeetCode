# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        s=[]
        if root is None:
            return []
        q=deque()
        q.append(root)
        while len(q)!=0:
            level_size=len(q)
            t=[]
            for i in range(level_size):
                ce=q.popleft()
                t.append(ce.val)
                if ce.left is not None:
                    q.append(ce.left)
                if ce.right is not None:
                    q.append(ce.right)
            
            s.append(t)
        return s[::-1]
        