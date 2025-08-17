# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0  
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal diam
            if not node:
                return 0
            lh = dfs(node.left)   
            rh = dfs(node.right)  

            # (lh - 1) + (rh - 1) + 2  ==  lh + rh
            diam = max(diam, lh + rh)
            return 1 + max(lh, rh)

        dfs(root)
        return diam