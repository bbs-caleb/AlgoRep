1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def longestZigZag(self, root: Optional[TreeNode]) -> int:
9        self.ans = 0
10
11        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
12            if not node:
13                return (0, 0)
14
15            left_goLeft, left_goRight = dfs(node.left)
16            right_goLeft, right_goRight = dfs(node.right)
17
18            goLeft = 1 + left_goRight if node.left else 0
19            goRight = 1 + right_goLeft if node.right else 0
20
21            self.ans = max(self.ans, goLeft, goRight)
22            return (goLeft, goRight)
23
24        dfs(root)
25        return self.ans
26