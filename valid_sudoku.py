# https://leetcode.com/problems/valid-sudoku/
def check_valid_sudoku(board):
    sudoku_checked = set()
    for rid, row in enumerate(board):
        for cid, val in enumerate(row):
            if val == ".":
                continue
            rentry = "{} in row {}".format(val, rid)
            centry = "{} in col {}".format(val, cid)
            boxentry = "{} in box {}{}".format(val, rid // 3, cid // 3)
            if (
                rentry in sudoku_checked
                or centry in sudoku_checked
                or boxentry in sudoku_checked
            ):
                return False

            sudoku_checked = sudoku_checked.union({rentry, centry, boxentry})
    return True


# board = [
#     ["8", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
# ]
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(check_valid_sudoku(board))
