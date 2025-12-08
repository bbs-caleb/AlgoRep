1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
9        self.max_depth = -1
10        self.answer = root.val 
11
12        def dfs(node, depth):
13            if node is None:
14                return 
15            
16            if depth > self.max_depth: 
17                self.max_depth = depth
18                self.answer = node.val
19            
20            dfs(node.left, depth + 1)
21            dfs(node.right, depth + 1)
22
23        dfs(root, 0)
24        return self.answer