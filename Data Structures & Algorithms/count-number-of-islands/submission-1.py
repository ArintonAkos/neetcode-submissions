class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        n_islands = 0

        m, n = len(grid), len(grid[0])
        
        def dfs(i: int, j: int):
            nonlocal m, n
            
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if grid[i][j] != "1":
                return

            grid[i][j] = "0"
            for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                dfs(x + i, y + j)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    n_islands += 1
                    dfs(i, j)
        
        return n_islands