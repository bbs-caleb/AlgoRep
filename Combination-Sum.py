1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        result = []
4        n = len(candidates)
5
6        def backtrack(start, current_path, current_sum):
7            if current_sum == target:
8                result.append(current_path[:])
9                return
10            
11            if current_sum > target:
12                return
13
14            for i in range(start, n):
15                num = candidates[i]
16                current_path.append(num)
17                backtrack(i, current_path, current_sum + num)
18                current_path.pop()
19
20        backtrack(0, [], 0)
21        return result