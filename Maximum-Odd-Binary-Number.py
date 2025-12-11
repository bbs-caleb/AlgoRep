1class Solution:
2    def maximumOddBinaryNumber(self, s: str) -> str:
3        n = len(s)
4        ones = s.count('1')
5        zeros = n - ones
6        prefix = '1' * (ones - 1)
7        middle = '0' * zeros
8        last = '1'
9        
10        return prefix + middle + last
11