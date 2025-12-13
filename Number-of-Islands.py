1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        if not grid:
4            return 0
5            
6        rows, cols = len(grid), len(grid[0])
7        count = 0
8        def dfs_sink(r, c):
9            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
10                return
11            
12            grid[r][c] = "0"
13            
14            dfs_sink(r + 1, c)
15            dfs_sink(r - 1, c)
16            dfs_sink(r, c + 1)
17            dfs_sink(r, c - 1)
18        
19        for r in range(rows):
20            for c in range(cols):
21                if grid[r][c] == "1":
22                    count += 1
23                    dfs_sink(r, c)
24        return count