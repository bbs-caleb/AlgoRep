class Solution:
    def getTargetCopy(self, original: 'TreeNode', cloned: 'TreeNode', target: 'TreeNode') -> 'TreeNode':
        stack = [(original, cloned)]
        while stack:
            o, c = stack.pop()
            if o is None:
                continue
            if o is target:
                return c
            stack.append((o.left, c.left))
            stack.append((o.right, c.right))
        return None  