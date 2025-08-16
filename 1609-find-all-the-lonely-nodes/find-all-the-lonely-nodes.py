# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        result = []

        while stack:
            node = stack.pop()

            if (node.left and node.right is None) or (node.left is None and node.right):
                if node.left:
                    result.append(node.left.val)
                if node.right:
                    result.append(node.right.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result 