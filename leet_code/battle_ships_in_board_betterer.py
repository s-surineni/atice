def count_ships(board):
    ship_count = 0
    for rid, row in enumerate(board):
        for cid, val in enumerate(row):
            if val == 'X':
                if rid > 0 and board[rid - 1][cid] == 'X':
                    continue
                if cid > 0 and board[rid][cid - 1] == 'X':
                    continue
                ship_count += 1
                # sink(board, rid, cid, r_len, c_len)
    return ship_count


board = [
    ['X', '.', '.', 'X'],
    ['.', '.', '.', 'X'],
    ['.', '.', '.', 'X']
]
print(count_ships(board))

