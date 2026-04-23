class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        cache = {}

        def dfs(i: int, j: int) -> bool:
            if j >= n:
                return i >= m

            if (i, j) in cache:
                return cache[(i, j)]

            first_match  = i < m and (p[j] == s[i] or p[j] == '.')

            # Look-ahead
            if j + 1 < n and p[j + 1] == '*':
                # Either matches the character 1 or more time
                # or it doesn't match at all and we can skip this pattern
                ans = (first_match and dfs(i + 1, j)) or dfs(i, j + 2)
            else:
                ans = (first_match and dfs(i + 1, j + 1))

            cache[(i, j)] = ans
            return ans

        return dfs(0, 0)
