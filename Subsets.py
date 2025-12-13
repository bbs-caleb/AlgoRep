1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        result = []
4        n = len(nums)
5
6        def backtrack(i, current_subset):
7            if i == n:
8                result.append(current_subset[:])
9                return
10
11            current_subset.append(nums[i])
12            backtrack(i + 1, current_subset)
13            current_subset.pop()
14            backtrack(i + 1, current_subset)
15
16        backtrack(0, [])
17        return result