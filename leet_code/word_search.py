def find_if_word_exists_dfs(board, word, r, c):
    if not word:
        return True

    this_c = word[0]
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nr, nc = dr + r, dc + c
        if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
            if board[nr][nc] == this_c:
                board[nr][nc] = None
                outcome = find_if_word_exists_dfs(board, word[1:], nr, nc)
                if outcome:
                    return outcome
                board[nr][nc] = this_c
    return False


def find_if_word_exists(board, word):
    word = list(word)
    this_c = word[0]
    
    for rid, row in enumerate(board):
        for cid, val in enumerate(row):
            if board[rid][cid] == this_c:
                board[rid][cid] = None
                outcome = find_if_word_exists_dfs(board, word[1:],
                                                  rid, cid)
                if outcome:
                    return outcome
                board[rid][cid] = this_c
    return False


board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
# word = "ABCCED"
word = "SEE"  # true.
# word = "ABCB" # return false.
print(find_if_word_exists(board, word))
