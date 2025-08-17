# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans: List[str] = []
        if not root:
            return []

        def dfs(node: TreeNode, path: List[str]) -> None:
            path.append(str(node.val))
            if not node.left and not node.right:
                ans.append("->".join(path))
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
            path.pop()
        dfs(root, [])
        return ans 
            