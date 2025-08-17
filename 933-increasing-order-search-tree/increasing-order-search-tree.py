# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode()
        tail = dummy

        stack = []
        curr = root


        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            curr.left = None 
            tail.right = curr 
            tail = curr 
            curr = curr.right
        return dummy.right