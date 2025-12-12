1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
10        successor = None
11        current = root
12        
13        while current:
14            if current.val > p.val:
15                successor = current
16                current = current.left
17            else:
18                current = current.right
19        return successor