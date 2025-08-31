class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] < x:
                j = stack.pop()
                ans[j] = x
            stack.append(i)
        
        for i, x in enumerate(nums):
            if not stack:
                break
            while stack and nums[stack[-1]] < x:
                j = stack.pop()
                ans[j] = x
        return ans 