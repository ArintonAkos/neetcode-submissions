class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: 
            return 0
        
        m, n = len(matrix), len(matrix[0])
        cache = {}

        def dfs(i: int, j: int):
            if (i, j) in cache:
                return cache[(i, j)]

            max_dist = 0
            for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                new_i, new_j = x + i, y + j

                if new_i < 0 or new_j < 0 or new_i >= m or new_j >= n:
                    continue

                if matrix[i][j] < matrix[new_i][new_j]:
                    max_dist = max(max_dist, dfs(new_i, new_j))

            cache[(i, j)] = max_dist + 1
            return cache[(i, j)]

        max_length = 0
        for i in range(m):
            for j in range(n):
                max_length = max(max_length, dfs(i, j))

        return max_length

                
        
            

