import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        m, n = len(grid), len(grid[0])

        def neighbours(i: int, j: int):
            for x_i, x_j in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                new_i, new_j = i + x_i, j + x_j
                
                if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                    continue

                val = grid[new_i][new_j]

                if val < 0:
                    continue

                yield val, new_i, new_j
                # No need to add the edges back, since the current vertex has already been visited

        def isLastRow(i: int, j: int) -> bool:
            return i == m - 1 and j == n - 1

        curr_max = grid[0][0]
        while heap:
            w, i, j = heapq.heappop(heap)

            if isLastRow(i, j):
                return w
        
            for new_w, new_i, new_j in neighbours(i, j):
                heapq.heappush(heap, (max(w, new_w), new_i, new_j))

            grid[i][j] = -1

        return -1
