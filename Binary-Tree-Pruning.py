1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        if not root:
10            return None
11        
12        root.left = self.pruneTree(root.left)
13        root.right = self.pruneTree(root.right)
14        
15        if root.val == 0 and not root.left and not root.right:
16            return None
17        return root
18        