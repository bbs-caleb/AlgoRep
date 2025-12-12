1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        stack = []
10        node = root
11
12        while node or stack:
13            while node:
14                stack.append(node)
15                node = node.left
16            node = stack.pop()
17            k -= 1
18            if k == 0:
19                return node.val
20            node = node.right