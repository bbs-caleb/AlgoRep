1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
9        if not root:
10            return None
11        
12        if root.val < low:
13            return self.trimBST(root.right, low, high)
14        
15        if root.val > high:
16            return self.trimBST(root.left, low, high)
17        
18        root.left = self.trimBST(root.left, low, high)
19        root.right = self.trimBST(root.right, low, high)
20        return root