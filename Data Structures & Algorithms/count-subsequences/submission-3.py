class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        cache = {}

        def dfs(i: int, j: int) -> int:
            if j == n:
                return 1

            if i == m:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == t[j]:
                res = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                res = dfs(i + 1, j)
 
            cache[(i, j)] = res
            return cache[(i, j)]
        
        return dfs(0, 0)