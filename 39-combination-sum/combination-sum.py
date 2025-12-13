class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)

        def backtrack(start, current_path, current_sum):
            if current_sum == target:
                result.append(current_path[:])
                return
            
            if current_sum > target:
                return

            for i in range(start, n):
                num = candidates[i]
                current_path.append(num)
                backtrack(i, current_path, current_sum + num)
                current_path.pop()

        backtrack(0, [], 0)
        return result