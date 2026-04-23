class Solution:


    def numIslands(self, grid: List[List[str]]) -> int:
        n_islands = 0
        m, n = len(grid), len(grid[0])

        def floodFill(i: int, j: int):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if grid[i][j] == "0":
                return

            grid[i][j] = "0"

            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_i, new_j = i + x, j + y
                floodFill(new_i, new_j)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    n_islands += 1
                    floodFill(i, j)

        return n_islands