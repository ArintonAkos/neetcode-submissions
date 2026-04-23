class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        def bfs(i: int, j: int):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if board[i][j] != 'O':
                return

            # Temporarily set it to S to note which ones survive (accessible from edge)
            board[i][j] = 'S'

            for x, y in ([-1, 0], [0, -1], [1, 0], [0, 1]):
                new_i, new_j = i + x, j + y
                bfs(new_i, new_j)

        for i in range(m):
            bfs(i, 0)
            bfs(i, n - 1)

        for j in range(n):
            bfs(0, j)
            bfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'

        



            