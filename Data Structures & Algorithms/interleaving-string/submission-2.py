class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False
            
        # n rows, m columns
        grid = [[False] * (m + 1) for _ in range(n + 1)]

        grid[0][0] = True

        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    continue

                p = i + j - 1

                if i == 0:
                    grid[i][j] = s3[p] == s1[j - 1] and grid[i][j - 1]
                elif j == 0:
                    grid[i][j] = s3[p] == s2[i - 1] and grid[i - 1][j]
                else:
                    match_s1 = s3[p] == s1[j - 1] and grid[i][j - 1]
                    match_s2 = s3[p] == s2[i - 1] and grid[i - 1][j]
                    
                    grid[i][j] = match_s1 or match_s2

        print(f"Grid: {grid}")
        return grid[n][m]