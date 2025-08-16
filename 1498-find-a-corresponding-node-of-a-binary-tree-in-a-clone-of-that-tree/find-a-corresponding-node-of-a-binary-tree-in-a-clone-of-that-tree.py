class Solution:
    def getTargetCopy(self, original: 'TreeNode', cloned: 'TreeNode', target: 'TreeNode') -> 'TreeNode':
        from collections import deque 

        if not original:
            return None
        
        stack = deque([(original, cloned)])
        while stack:
            o, c = stack.popleft()
            if o is target:
                return c
            else:
                if o.left:
                    stack.append((o.left, c.left))
                if o.right:
                    stack.append((o.right, c.right))
        
        