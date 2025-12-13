class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        count = 0
        def dfs_sink(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            
            dfs_sink(r + 1, c)
            dfs_sink(r - 1, c)
            dfs_sink(r, c + 1)
            dfs_sink(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs_sink(r, c)
        return count