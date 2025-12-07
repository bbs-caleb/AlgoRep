# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            hl = height(node.left)
            if hl == -1:
                return -1
            hr = height(node.right)
            if hr == -1:
                return -1
            if abs(hl - hr) > 1:
                return -1 
            return 1 + max(hl, hr)
        return height(root) != -1
