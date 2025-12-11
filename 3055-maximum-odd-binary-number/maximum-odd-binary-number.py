class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ones = s.count('1')
        zeros = n - ones
        prefix = '1' * (ones - 1)
        middle = '0' * zeros
        last = '1'
        
        return prefix + middle + last
