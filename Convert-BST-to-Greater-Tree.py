1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        total = 0
10        stack = []
11        node = root
12
13        while node or stack:
14            while node:
15                stack.append(node)
16                node = node.right
17
18            node = stack.pop()
19            total += node.val
20            node.val = total
21
22            node = node.left
23        return root
24