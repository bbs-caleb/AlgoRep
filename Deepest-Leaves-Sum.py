1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11        
12        queue = deque([root])
13        deepest_sum = 0
14
15        while queue:
16            level_size = len(queue)
17            level_sum = 0
18
19            for _ in range(level_size):
20                node = queue.popleft()
21                level_sum += node.val
22
23                if node.left is not None:
24                    queue.append(node.left)
25                if node.right is not None:
26                    queue.append(node.right)
27            deepest_sum = level_sum
28        return deepest_sum