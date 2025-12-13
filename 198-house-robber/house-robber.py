class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        prev2 = 0
        prev1 = 0
        
        for money in nums:
            current_max = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = current_max
            
        return prev1