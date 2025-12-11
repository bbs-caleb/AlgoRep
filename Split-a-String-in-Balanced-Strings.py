1class Solution:
2    def balancedStringSplit(self, s: str) -> int:
3        balance = 0
4        ans = 0
5        
6        for char in s:
7            if char == 'L':
8                balance += 1
9            else:
10                balance -= 1
11            
12            if balance == 0:
13                ans += 1
14                
15        return ans