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
11        total = 0
12        
13        if low <= root.val <= high:
14            total += root.val
15        
16        if root.val > low:
17            total += self.rangeSumBST(root.left, low, high)
18        if root.val < high:
19            total += self.rangeSumBST(root.right, low, high)
20        return total 
21
22