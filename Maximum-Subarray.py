1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        current_sum = nums[0]
4        max_sum = nums[0]
5
6        for num in nums[1:]:
7            current_sum = max(num, current_sum + num)
8            max_sum = max(max_sum, current_sum)
9        return max_sum