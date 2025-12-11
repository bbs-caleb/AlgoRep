1class Solution:
2    def maximum69Number (self, num: int) -> int:
3        num = list(str(num))
4        for i in range(len(num)):
5            if num[i] == '6':
6                num[i] = '9'
7                return int(''.join(num))
8        return int(''.join(num))