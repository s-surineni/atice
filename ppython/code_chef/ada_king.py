# https://www.codechef.com/JULY20B/problems/ADAKING
def find_factors(moves):

    for ln in range(2, 9):
        br = (moves // ln) + 1
        if ln > 8 or 8 < br:
            ln += 1
        else:
            return ln, br
    return 8, 8


def print_board(chess_board):
    for row in chess_board:
        for val in row:
            print(val, end=' ')
        print()
    print()

tc = int(input().strip())


# print(chess_board)
for _ in range(tc):
    chess_board = [['.'] * 8 for i in range(8)]
    chess_board[0][0] = 'O'
    moves = int(input().strip())
    if moves == 64:
        print_board(chess_board)
        break
    # print(moves)
    ln, br = find_factors(moves)
    print(ln, br)
    for cl in range(br + 1):
        chess_board[ln][cl] = 'X'
    for rw in range(ln + 1):
        chess_board[rw][br] = 'X'

    extra_cells = ln * br - moves
    for ri in range(ln):
        for ci in range(br):
            if chess_board[ri][ci] == '.':
                chess_board[ri][ci] = 'X'
                extra_cells -= 1
            if not extra_cells:
                break
        if not extra_cells:
            break
    print_board(chess_board)
