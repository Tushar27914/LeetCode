# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth=0
        if root is None:
            return 0
        q=deque([])
        q.append(root)
        while len(q)!=0:
            max_depth+=1
            level_size=len(q)
            for i in range(level_size):
                ce=q.popleft()
                if ce.left is not None:
                    q.append(ce.left)
                if ce.right is not None:
                    q.append(ce.right)
        return max_depth
        