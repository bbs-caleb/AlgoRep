# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.all_sums = []
        
        def dfs_sum(node):
            if not node:
                return 0

            current_subtree_sum = node.val + dfs_sum(node.left) + dfs_sum(node.right)
            
            self.all_sums.append(current_subtree_sum)
            return current_subtree_sum
        
        total_sum = dfs_sum(root)
        max_prod = 0
        
        for s in self.all_sums:
            current_prod = s * (total_sum - s)
            max_prod = max(max_prod, current_prod)
            
        return max_prod % (10**9 + 7)