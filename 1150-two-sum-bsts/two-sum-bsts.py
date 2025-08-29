# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        if not root1 or not root2:
            return False
        
        seen1 = set()
        stack = [root1]

        while stack:
            node = stack.pop()        
            if not node:
                continue
            seen1.add(node.val)

            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)

        stack = [root2]

        while stack:
            node = stack.pop()
            if not node:
                continue
            if target - node.val in seen1:
                return True 

            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return False 