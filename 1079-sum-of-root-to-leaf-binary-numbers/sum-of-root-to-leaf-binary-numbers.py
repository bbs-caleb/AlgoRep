# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0
        path = []

        def dfs(node):
            nonlocal ans
            if not node:
                return
            path.append(str(node.val))

            if not node.left and not node.right: 
                ans += int("".join(path), 2)
            else:
                dfs(node.left)
                dfs(node.right)

            path.pop()  

        dfs(root)
        return ans