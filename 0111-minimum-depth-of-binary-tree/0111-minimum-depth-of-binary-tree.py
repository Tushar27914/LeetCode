# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        minimum_depth=0
        if root is None:
            return 0
        q=deque()
        q.append(root)
        while len(q)!=0:
            minimum_depth+=1
            level_size=len(q)
            for i in range(level_size):
                ce=q.popleft()
                if ce.left is None and ce.right is None:
                    return minimum_depth
                if ce.left is not None:
                    q.append(ce.left)
                if ce.right is not None:
                    q.append(ce.right)
        return minimum_depth
        