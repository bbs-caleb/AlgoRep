1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def averageOfSubtree(self, root: TreeNode) -> int:
9        self.answer = 0
10
11        def dfs(node): 
12            if node is None:
13                return 0, 0
14
15            left_sum, left_count = dfs(node.left)
16            right_sum, right_count = dfs(node.right)
17
18            total_sum = left_sum + right_sum + node.val
19            total_count = left_count + right_count + 1
20
21            avg = total_sum // total_count
22
23            if avg == node.val:
24                self.answer += 1 
25            
26            return total_sum, total_count
27        
28        dfs(root)
29        return self.answer 