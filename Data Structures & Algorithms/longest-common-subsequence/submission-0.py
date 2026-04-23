class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        grid = [[0] * (m + 1) for _ in range(n + 1)]

        # n number of rows
        # m number of cols
        for i in range(n):
            for j in range(m):
                if text1[j] == text2[i]:
                    grid[i + 1][j + 1] = 1 + grid[i][j]
                else:
                    grid[i + 1][j + 1] = max(grid[i][j + 1], grid[i + 1][j])

        return grid[n][m]