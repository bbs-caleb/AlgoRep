# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque 

        if root is None:
            return None 

        stack = deque([root])
        while stack:
            node = stack.popleft()
            node.right, node.left = node.left, node.right 
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root 