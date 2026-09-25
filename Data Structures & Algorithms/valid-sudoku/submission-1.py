class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checking each row
        temp_dict_row = {}
        for i in range(len(board)):
            for j in range(len(board)):
                elem = board[i][j]
                if elem in list(temp_dict_row.keys()):
                    if elem == ".":
                        pass
                    else:
                        return False
                else:
                    temp_dict_row[elem] = 1
            temp_dict_row = {}

        # checking each col

        temp_dict_col = {}
        for i in range(len(board)):
            for j in range(len(board)):
                elem = board[j][i]
                if elem in list(temp_dict_col.keys()):
                    if elem == ".":
                        pass
                    else:
                        return False
                else:
                    temp_dict_col[elem] = 1
            temp_dict_col = {}

        # checking grids
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                temp_dict_grid = {}

                for i in range(row_start, row_start + 3):
                    for j in range(col_start, col_start + 3):
                        elem = board[i][j]

                        if elem == ".":
                            continue

                        if elem in temp_dict_grid:
                            return False

                        temp_dict_grid[elem] = 1

        return True





