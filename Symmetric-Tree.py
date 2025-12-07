1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
9        if root is None:
10            return None 
11        
12        def dfs(left, right):
13            if not left and not right:
14                return True 
15            if not left or not right:
16                return False
17            if left.val != right.val:
18                return False
19            return (dfs(left.left, right.right) 
20                            and dfs(left.right, right.left))
21        return dfs(root.left, root.right)
22