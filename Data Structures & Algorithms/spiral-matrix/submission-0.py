class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        # When we hit a boundary, change direction
        dir_idx = 3
        m, n = len(matrix), len(matrix[0])
        res = []

        def dfs(i: int, j: int):
            if i < 0 or j < 0 or i >= m or j >= n:
                return

            if matrix[i][j] == float('inf'):
                return

            nonlocal dir_idx

            res.append(matrix[i][j])
            matrix[i][j] = float('inf')
            
            # Check next item in direction
            x, y = dirs[dir_idx]
            new_i, new_j = x + i, y + j

            # Check boundary or already visited item
            if new_i < 0 or new_j < 0 or new_i >= m or new_j >= n or matrix[new_i][new_j] == float('inf'):
                dir_idx = (dir_idx + 1) % 4
                x, y = dirs[dir_idx]
                new_i, new_j = x + i, y + j

            dfs(new_i, new_j)

        dfs(0, 0)

        return res