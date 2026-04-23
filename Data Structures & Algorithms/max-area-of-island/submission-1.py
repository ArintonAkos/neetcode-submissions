class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_sum = 0
        self.curr_sum = 0
        m, n = len(grid), len(grid[0])

        def floodFill(i: int, j: int):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if grid[i][j] == 0:
                return

            grid[i][j] = 0
            self.curr_sum += 1
            self.max_sum = max(self.curr_sum, self.max_sum)

            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_i, new_j = i + x, j + y
                floodFill(new_i, new_j)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.curr_sum = 0
                    floodFill(i, j)

        return self.max_sum
