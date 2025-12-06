1from typing import List 
2# Definition for a binary tree node.
3# class TreeNode:
4#     def __init__(self, val=0, left=None, right=None):
5#         self.val = val
6#         self.left = left
7#         self.right = right
8class Solution:
9    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
10        result: List[int] = []
11
12        def dfs(node):
13            if node is None:
14                return 
15            
16            if node.left is not None and node.right is None:
17                result.append(node.left.val)
18            
19            if node.right is not None and node.left is None:
20                result.append(node.right.val)
21            
22            dfs(node.left)
23            dfs(node.right)
24        dfs(root)
25        return result 