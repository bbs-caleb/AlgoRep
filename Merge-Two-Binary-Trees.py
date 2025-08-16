# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque

        if not root1: return root2
        if not root2: return root1

        q = deque([(root1, root2)])

        while q:
            u, v = q.popleft()
            u.val += v.val

            if not u.left:
                u.left = v.left 
            else:
                if v.left:
                    q.append((u.left, v.left))
            
            if not u.right:
                u.right = v.right
            else:
                if v.right:
                    q.append((u.right, v.right))
        
        return root1 
