1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        answer = nums[0]
4        max_prod = nums[0]
5        min_prod = nums[0]
6
7        for num in nums[1:]:
8            a = num * max_prod 
9            b = num * min_prod 
10            min_prod = min(num, a, b)
11            max_prod = max(num, a, b)
12            answer = max(answer, max_prod)
13        return answer