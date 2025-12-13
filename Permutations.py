1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        res = []
4        n = len(nums)
5        used = [False] * n
6        path: List[int] = []
7
8        def dfs():
9            if len(path) == n:
10                res.append(path.copy())
11                return
12
13            for i in range(n):
14                if used[i]:
15                    continue
16                used[i] = True
17                path.append(nums[i])
18                dfs()
19                path.pop()
20                used[i] = False
21        dfs()
22        return res
23
24
25        