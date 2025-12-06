1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
9        if root is None:
10            return 0 
11
12        total = 0
13        stack = [root]
14
15        while stack:
16            node = stack.pop()
17
18            if node is None:
19                continue 
20
21            if low <= node.val <= high:
22                total += node.val 
23            
24            if node.val > low:
25                stack.append(node.left)
26            
27            if node.val < high:
28                stack.append(node.right)
29        return total 
30
31            
32