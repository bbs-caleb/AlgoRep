1class Solution:
2    def smallestNumber(self, pattern: str) -> str:
3        res = []
4        stack = []
5        
6
7        for i in range(len(pattern) + 1):
8            stack.append(str(i + 1))
9            if i == len(pattern) or pattern[i] == 'I':
10                while stack:
11                    res.append(stack.pop())
12        return "".join(res)