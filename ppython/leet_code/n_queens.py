def find_n_queens_positions_recur(q_count, curr_row, q_positions):
    if q_count == curr_row:
        return True

    for col in range(q_count):
        # this is special because for first row we wont enter the below for loop
        # initializing this to be true is necessary
        found_safe = True

        for a_row in range(curr_row):
            # this is special too because for a column we MUST
            # check it is safe with all the rows
            if (q_positions[a_row][1] == col
                or q_positions[a_row][0] - q_positions[a_row][1] == curr_row - col
                or q_positions[a_row][0] + q_positions[a_row][1] == curr_row + col):
                found_safe = False
                break

        if found_safe:
            q_positions[curr_row] = (curr_row, col)
            if find_n_queens_positions_recur(q_count,
                                             curr_row + 1,
                                             q_positions):
                return True
    return False

def find_n_queens_positions(q_count):
    q_positions = [None] * q_count
    find_n_queens_positions_recur(q_count, 0, q_positions)
    return q_positions


if __name__ == '__main__':
    print(find_n_queens_positions(3))
