# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode()
        self.tail = dummy

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            node.left = None
            self.tail.right = node
            self.tail = node 
            inorder(node.right)

        inorder(root)
        return dummy.right
