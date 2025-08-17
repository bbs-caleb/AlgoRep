# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return
            if (node.left is None) ^ (node.right is None):
                if (node.left and node.right is None):
                    res.append(node.left.val)
                if (node.left is None and node.right):
                    res.append(node.right.val)

            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res 