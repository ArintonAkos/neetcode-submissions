class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not grid[i][j]:
                    continue
                
                res += 4

                if i - 1 >= 0 and grid[i - 1][j]:
                    res -= 2
                if j - 1 >= 0 and grid[i][j - 1]:
                    res -= 2

        return res

                