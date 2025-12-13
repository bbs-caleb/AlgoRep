class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtrack(i, current_subset):
            if i == n:
                result.append(current_subset[:])
                return

            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()
            backtrack(i + 1, current_subset)

        backtrack(0, [])
        return result