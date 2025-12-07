1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        def depth(node):
10            if not node:
11                return 0
12            return 1 + max(depth(node.left), depth(node.right))
13        
14        if not root:
15            return True
16        if abs(depth(root.left) - depth(root.right)) > 1:
17            return False
18        return self.isBalanced(root.left) and self.isBalanced(root.right)
19
20
21        