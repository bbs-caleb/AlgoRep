# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left:
            return root
        q = deque([(root.left, root.right, 1)])
        while q:
            a, b, level = q.popleft()
            if not a: 
                continue
            if level % 2 == 1:
                a.val, b.val = b.val, a.val
            q.append((a.left,  b.right, level + 1))
            q.append((a.right, b.left,  level + 1))
        return root