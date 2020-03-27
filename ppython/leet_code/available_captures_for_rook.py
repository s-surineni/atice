def find_captures(board, ri, ci):
    pawn_count = 0
    # left side
    cip = ci - 1
    while cip > -1:
        # The order of if statements is important here <!note>
        if board[ri][cip] == 'p':
            pawn_count += 1
            break
        # instead of chacking for B, C, it was enough to see not presence of empty space <!note> <!better?
        if board[ri][cip] != '.':
            break
        cip -= 1
    # right side
    cip = ci + 1
    while cip < len(board[0]):
        if board[ri][cip] == 'p':
            pawn_count += 1
            break
        if board[ri][cip] != '.':
            break
        cip += 1
    rip = ri - 1
    while rip > -1:
        if board[rip][ci] == 'p':
            pawn_count += 1
            break
        if board[ri][cip] != '.':
            break
        rip -= 1
    rip = ri + 1
    while rip < len(board):
        if board[rip][ci] == 'p':
            pawn_count += 1
            break
        if board[rip][ci] != '.':
            break
        rip += 1   
    return pawn_count


class Solution:
    def numRookCaptures(self, board):
        for ri, row in enumerate(board):
            for ci, val in enumerate(row):
                if val == 'R':
                    return find_captures(board, ri, ci)


board = [[".",".",".",".",".",".",".","."],
         [".",".",".","p",".",".",".","."],
         [".",".",".","R",".",".",".","p"],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".","p",".",".",".","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".","."]]

print(Solution().numRookCaptures(board))
