1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        res = []
10
11        def dfs(node):
12            if not node:
13                return 
14            dfs(node.left)
15            res.append(node.val)
16            dfs(node.right)
17        dfs(root)
18        return res 