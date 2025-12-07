1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
10        queue = deque([(p, q)])
11        while queue:
12            n1, n2 = queue.popleft()
13
14            if not n1 and not n2:
15                continue
16            if not n1 or not n2:
17                return False
18            if n1.val != n2.val:
19                return False
20            
21            queue.append((n1.left, n2.left))
22            queue.append((n1.right, n2.right))
23        return True 
24
25