class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Frequencies
        row = [[0 for _ in range(9)] for _ in range(9)]
        col = [[0 for _ in range(9)] for _ in range(9)]
        box = [[0 for _ in range(9)] for _ in range(9)]

        def box_id(i: int, j: int):
            return 3 * ( i // 3 ) + ( j // 3 )

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                num = int(board[i][j]) - 1
                b_id = box_id(i, j)

                row[i][num] += 1
                col[j][num] += 1
                box[b_id][num] += 1

                # print(f"{row[i][num]} {col[j][num]} {box[b_id][num]} num: {num} i: {i} j: {j}")
                if row[i][num] > 1 or col[j][num] > 1 or box[b_id][num] > 1:
                    return False

        return True

        