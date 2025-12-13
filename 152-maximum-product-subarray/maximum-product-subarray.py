class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = nums[0]
        max_prod = nums[0]
        min_prod = nums[0]

        for num in nums[1:]:
            a = num * max_prod 
            b = num * min_prod 
            min_prod = min(num, a, b)
            max_prod = max(num, a, b)
            answer = max(answer, max_prod)
        return answer