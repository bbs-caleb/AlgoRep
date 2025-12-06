# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node_orig, node_clon):
            if node_orig is None:
                return None
            
            if node_orig is target:
                return node_clon
            
            left_res =  dfs(node_orig.left, node_clon.left)
            if left_res is not None:
                return left_res 
            
            right_res = dfs(node_orig.right, node_clon.right)
            if right_res is not None:
                return right_res 
            
        return dfs(original, cloned)