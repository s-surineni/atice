def find_horizontal_positions(rid, cid, ship_locations, board):
    for ncid in range(cid, len(board[0])):
        if board[rid][ncid] == 'X':
            ship_locations.add((rid, ncid))
        else:
            break


def find_vertical_positions(rid, cid, ship_locations, board):
    for rcid in range(rid, len(board)):
        if board[rcid][cid] == 'X':
            ship_locations.add((rcid, cid))
        else:
            break


def find_all_ship_parts(rid, cid, ship_locations, board):
    find_horizontal_positions(rid, cid, ship_locations, board)
    find_vertical_positions(rid, cid, ship_locations, board)


def count_ships(board):
    ship_locations = set()
    ship_count = 0
    for rid, row in enumerate(board):
        for cid, val in enumerate(row):
            if val == 'X':
                if (rid, cid) not in ship_locations:
                    find_all_ship_parts(rid, cid, ship_locations, board)
                    ship_count += 1
    return ship_count


board = [
    ['X', '.', '.', 'X'],
    ['.', '.', '.', 'X'],
    ['.', '.', '.', 'X']
]
print(count_ships(board))
