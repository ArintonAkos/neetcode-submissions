class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        cache = {}

        def dfs(i: int, j: int) -> int:
            if (i, j) in cache:
                return cache[(i, j)]

            if j == n:
                return 1

            sub_res = 0

            for s_i in range(i, m):
                if s[s_i] == t[j]:
                    sub_res += dfs(s_i + 1, j + 1)

            cache[(i, j)] = sub_res
            return cache[(i, j)]
        

        return dfs(0, 0)