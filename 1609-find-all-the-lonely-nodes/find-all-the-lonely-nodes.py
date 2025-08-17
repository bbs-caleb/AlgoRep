# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        q = deque([root])

        while q:
            node = q.popleft()
            if (node.left is None) ^ (node.right is None):
                lonely = node.left if node.right is None else node.right
                ans.append(lonely.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans 