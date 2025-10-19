class Solution:
    def isBalanced(self, node: Optional[TreeNode]) -> bool:
        def depth(node):
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))

        if not node:
            return True
        if abs(depth(node.left) - depth(node.right)) > 1:
            return False
        return self.isBalanced(node.left) and self.isBalanced(node.right)
