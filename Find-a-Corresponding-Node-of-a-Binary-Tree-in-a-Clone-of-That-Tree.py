1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
10        def dfs(node_orig, node_clon):
11            if node_orig is None:
12                return None
13            
14            if node_orig is target:
15                return node_clon
16            
17            left_res =  dfs(node_orig.left, node_clon.left)
18            if left_res is not None:
19                return left_res 
20            
21            right_res = dfs(node_orig.right, node_clon.right)
22            if right_res is not None:
23                return right_res 
24            
25        return dfs(original, cloned)