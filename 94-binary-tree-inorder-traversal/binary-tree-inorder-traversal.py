# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        RES = []
        def DFS(NODE):
            if not NODE:
                return 
            DFS(NODE.left)
            RES.append(NODE.val)
            DFS(NODE.right)
        DFS(root)
        return RES 