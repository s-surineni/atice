# https://leetcode.com/problems/surrounded-regions/
def swap_OZ(board, row, col):
    row_count = len(board)
    col_count = len(board[0])
    stack = [(row, col)]
    while stack:
        nodex, nodey = stack.pop()
        board[nodex][nodey] = "Z"
        for x, y in (
            (nodex + 1, nodey),
            (nodex - 1, nodey),
            (nodex, nodey + 1),
            (nodex, nodey - 1),
        ):
            if 0 <= x < row_count and 0 <= y < col_count:
                if board[x][y] == "O":
                    stack.append((x, y))


def capture(board):
    for rid, row in enumerate(board):
        for cid, val in enumerate(row):
            if board[rid][cid] == "O":
                board[rid][cid] = "X"
            elif board[rid][cid] == "Z":
                board[rid][cid] = "O"


def find_surrounded_regions(board):
    row_count = len(board)
    col_count = len(board[0])

    for row in (0, row_count - 1):
        for col in range(col_count):
            if board[row][col] == "O":
                swap_OZ(board, row, col)

    for col in (0, col_count - 1):
        for row in range(row_count):
            if board[row][col] == "O":
                swap_OZ(board, row, col)

    capture(board)


board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]
find_surrounded_regions(board)
print(board)
