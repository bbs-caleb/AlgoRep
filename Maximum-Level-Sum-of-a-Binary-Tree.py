1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11        
12        level_sums: Dict[int, int] = {}
13
14        def dfs(node, level):
15            if not node:
16                return
17
18            level_sums[level] = level_sums.get(level, 0) + node.val
19
20            dfs(node.left, level + 1)
21            dfs(node.right, level + 1)
22        
23        dfs(root, 1)
24
25        max_sum = float('-inf')
26        best_level = 1
27
28        for level, s in level_sums.items():
29            if s > max_sum or (s ==  max_sum and level < best_level):
30                max_sum = s
31                best_level = level
32
33        return best_level 