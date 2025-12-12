# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        current = root
        
        while current:
            if current.val > p.val:
                successor = current
                current = current.left
            else:
                current = current.right
        return successor