class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_set = set()
            for val in row:
                if val == '.': 
                    continue
                if val in row_set: 
                    return False
                row_set.add(val)
        for i in range(9):
            col_set = set()
            for col_i in range(9):
                val = board[col_i][i]
                if val == '.':
                    continue
                if val in col_set:
                    return False
                col_set.add(val)
        for start_row in range(0, 7, 3):
            three_rows = board[start_row:start_row+3]
            for i in range(0,7,3):
                box = []
                box_set = set()
                for row in three_rows:
                    box_row_vals = row[i:i+3]
                    for val in box_row_vals:
                        if val == '.': 
                            continue
                        if val in box_set: 
                            return False
                        box_set.add(val)
        return True