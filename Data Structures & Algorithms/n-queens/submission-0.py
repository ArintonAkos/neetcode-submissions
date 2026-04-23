class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [False] * n
        l_diag = [False] * (2 * n - 1)
        r_diag = [False] * (2 * n - 1)

        # Return the index of the diagonal
        # Can be used for retrieving whether a queen is watching the diagon or not
        def get_l_diag_idx(i: int, j: int) -> int:
            return n - i + j - 1

        # Return the index of the diagonal
        # Can be used for retrieving whether a queen is watching the diagon or not
        def get_r_diag_idx(i: int, j: int) -> int:
            return i + j

        res: List[List[str]] = []
        line: List[str] = ["." for _ in range(n)]

        def backtrack(sub_res: List[str]):
            if len(sub_res) == n:
                res.append(sub_res.copy())
                return

            # i -> row index
            i = len(sub_res)
            for j in range(n):
                l_diag_idx = get_l_diag_idx(i, j)
                r_diag_idx = get_r_diag_idx(i, j)

                if not cols[j] and not l_diag[l_diag_idx] and not r_diag[r_diag_idx]:
                    cols[j] = True
                    l_diag[l_diag_idx] = True
                    r_diag[r_diag_idx] = True

                    line[j] = "Q"
                    sub_res.append("".join(line))
                    line[j] = "."

                    backtrack(sub_res)

                    sub_res.pop()
                    l_diag[l_diag_idx] = False
                    r_diag[r_diag_idx] = False    
                    cols[j] = False

        backtrack([])

        return res