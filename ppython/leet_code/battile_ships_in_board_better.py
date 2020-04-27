def sink(board, rid, cid, r_len, c_len):
    if r_len > rid >= 0 <= cid < c_len and board[rid][cid] == 'X':
        board[rid][cid] = '.'
        sink(board, rid + 1, cid, r_len, c_len)
        sink(board, rid, cid + 1, r_len, c_len)


def count_ships(board):
    r_len = len(board)
    c_len = len(board[0])
    ship_count = 0
    for rid, row in enumerate(board):
        for cid, val in enumerate(row):
            if val == 'X':
                ship_count += 1
                sink(board, rid, cid, r_len, c_len)
    return ship_count


board = [
    ['X', '.', '.', 'X'],
    ['.', '.', '.', 'X'],
    ['.', '.', '.', 'X']
]
print(count_ships(board))
