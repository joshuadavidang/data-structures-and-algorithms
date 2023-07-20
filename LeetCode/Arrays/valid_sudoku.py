def isValidSudoku(board):
    def is_valid_row(row):
        row_seen = {}
        for num in row:
            if num != ".":
                if num in row_seen:
                    return False
                row_seen[num] = 1
        return True

    def is_valid_column(col):
        col_seen = {}
        for i in range(9):
            num = board[i][col]
            if num != ".":
                if num in col_seen:
                    return False
                col_seen[num] = 1
        return True

    def is_valid_subbox(row, col):
        sub_box_seen = {}
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                num = board[i][j]
                if num != ".":
                    if num in sub_box_seen:
                        return False
                    sub_box_seen[num] = 1
        return True

    for i in range(9):
        if not is_valid_row(board[i]):
            return False

    for j in range(9):
        if not is_valid_column(j):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not is_valid_subbox(i, j):
                return False

    return True
