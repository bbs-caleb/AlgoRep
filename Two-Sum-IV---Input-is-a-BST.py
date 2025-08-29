# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = {}
        stack = [root]

        while stack:
            node = stack.pop()

            if node.val in seen.keys():
                return True
            else:
                seen[k - node.val] = 1
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False 