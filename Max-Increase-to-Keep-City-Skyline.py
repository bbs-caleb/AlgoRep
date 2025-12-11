1from typing import List
2
3class Solution:
4    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
5        n = len(grid)
6        row_max = [max(row) for row in grid]
7        
8        col_max = [max(grid[r][c] for r in range(n)) for c in range(n)]
9        
10        total_increase = 0
11        for r in range(n):
12            for c in range(n):
13                allowed = min(row_max[r], col_max[c])
14                total_increase += allowed - grid[r][c]
15        return total_increase
16
17
18
19