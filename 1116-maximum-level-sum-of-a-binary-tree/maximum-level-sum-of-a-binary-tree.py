# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level_sums: Dict[int, int] = {}

        def dfs(node, level):
            if not node:
                return

            level_sums[level] = level_sums.get(level, 0) + node.val

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 1)

        max_sum = float('-inf')
        best_level = 1

        for level, s in level_sums.items():
            if s > max_sum or (s ==  max_sum and level < best_level):
                max_sum = s
                best_level = level

        return best_level 