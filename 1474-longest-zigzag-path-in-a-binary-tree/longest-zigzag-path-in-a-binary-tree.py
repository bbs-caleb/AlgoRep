# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node:
                return (0, 0)

            left_goLeft, left_goRight = dfs(node.left)
            right_goLeft, right_goRight = dfs(node.right)

            goLeft = 1 + left_goRight if node.left else 0
            goRight = 1 + right_goLeft if node.right else 0

            self.ans = max(self.ans, goLeft, goRight)
            return (goLeft, goRight)

        dfs(root)
        return self.ans
