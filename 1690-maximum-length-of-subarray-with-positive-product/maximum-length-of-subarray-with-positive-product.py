class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos,neg, ans = 0, 0, 0  
        
        for x in nums:
            if x == 0:
                pos = neg = 0
            elif x > 0:
                pos = pos + 1
                neg = neg + 1 if neg > 0 else 0
            else:  
                new_pos = neg + 1 if neg > 0 else 0
                new_neg = pos + 1
                pos, neg = new_pos, new_neg
            ans = max(ans, pos)
        return ans