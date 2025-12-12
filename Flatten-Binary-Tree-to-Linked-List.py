1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def flatten(self, root: Optional[TreeNode]) -> None:
9        """
10        Do not return anything, modify root in-place instead.
11        """
12        self.prev = None
13        
14        def dfs(node):
15            if not node:
16                return
17            
18            dfs(node.right)
19            
20            dfs(node.left)
21            node.right = self.prev
22            node.left = None
23            self.prev = node
24            
25        dfs(root)