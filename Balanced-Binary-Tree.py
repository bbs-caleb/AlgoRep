1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        def height(node):
10            if node is None:
11                return 0
12            hl = height(node.left)
13            if hl == -1:
14                return -1
15            hr = height(node.right)
16            if hr == -1:
17                return -1
18            if abs(hl - hr) > 1:
19                return -1 
20            return 1 + max(hl, hr)
21        return height(root) != -1
22