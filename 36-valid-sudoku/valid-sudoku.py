class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check duplicates in rows
        for row in board:
            row_count = {}
            for cell in row:
                if cell == ".":
                    continue  
                key = cell
                if key in row_count:
                    return False
                row_count[key] = 1

        # Check duplicates in columns
        for j in range(9):
            i = 0
            col_count = {}
            for i in range(9):
                key = board[i][j]
                if key == ".":
                    continue
                if key in col_count:
                    return False
                col_count[key] = 1

        # Check duplicates in 3x3 squares
        start_row = 0
        start_col = 0
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                seen = {}
                for row in board[start_row:start_row+3]:
                    for col in row[start_col:start_col+3]:
                        key = col
                        if key == ".":
                            continue
                        if key in seen:
                            return False
                        seen[key] = 1

        return True