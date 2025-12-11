1class Solution:
2    def minimumSum(self, num: int) -> int:
3        digits = sorted(int(ch) for ch in str(num))  
4        new1 = digits[0] * 10 + digits[2]
5        new2 = digits[1] * 10 + digits[3]
6        
7        return new1 + new2
8