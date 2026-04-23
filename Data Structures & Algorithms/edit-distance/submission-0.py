class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        cache = {}

        def dfs(i: int, j: int) -> int:
            if i < 0:
                return j + 1

            if j < 0:
                return i + 1

            if (i, j) in cache:
                return cache[(i, j)]

            if word1[i] == word2[j]:
                res = dfs(i - 1, j - 1)
            else:
                # If we insert we insert to the shorter -> the pointer remains the same
                # If we delte, we delete the longer
                # For replace, both has to be subtracted
                insert  = dfs(i, j - 1)
                delete  = dfs(i - 1, j)
                replace = dfs(i - 1, j - 1)

                res = 1 + min(insert, delete, replace)

            cache[(i, j)] = res
            return cache[(i, j)]
            
        return dfs(m - 1, n - 1)