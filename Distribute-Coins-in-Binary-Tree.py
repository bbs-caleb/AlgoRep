1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def distributeCoins(self, root: Optional[TreeNode]) -> int:
9        moves = 0
10
11        def dfs(node):
12            nonlocal moves
13            if not node:
14                return 0
15            l = dfs(node.left)
16            r = dfs(node.right)
17            moves += abs(l) + abs(r)
18            return (node.val - 1) + l + r
19
20        dfs(root)
21        return moves
22
23