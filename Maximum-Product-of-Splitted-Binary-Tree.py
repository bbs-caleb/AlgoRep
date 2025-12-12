1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxProduct(self, root: Optional[TreeNode]) -> int:
9        self.all_sums = []
10        
11        def dfs_sum(node):
12            if not node:
13                return 0
14
15            current_subtree_sum = node.val + dfs_sum(node.left) + dfs_sum(node.right)
16            
17            self.all_sums.append(current_subtree_sum)
18            return current_subtree_sum
19        
20        total_sum = dfs_sum(root)
21        max_prod = 0
22        
23        for s in self.all_sums:
24            current_prod = s * (total_sum - s)
25            max_prod = max(max_prod, current_prod)
26            
27        return max_prod % (10**9 + 7)