class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        max_d = 0

        while stack:
            node, d = stack.pop()
            if node:
                max_d = max(max_d, d)
                if node.left:
                    stack.append((node.left, d + 1))
                if node.right:
                    stack.append((node.right, d + 1))
        return max_d 