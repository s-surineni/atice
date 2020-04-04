from collections import deque


def find_solution(board):
    curr_config = ''.join(str(d) for row in board for d in row)
    rows = len(board)
    cols = len(board[0])
    board_states = deque()
    configs_seen = {(curr_config, curr_config.index('0'))}
    board_states.append((curr_config, curr_config.index('0')))

    steps = 0

    while board_states:
        for _ in range(len(board_states)):
            curr_config, z_idx = board_states.popleft()
            if curr_config == '123450': return steps
            ridx, cidx = z_idx // cols, z_idx % cols
            curr_config_list = list(curr_config)
            for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                next_config_list = curr_config_list[:]

                n_ridx, n_cidx = (ridx + x), (cidx + y)
                if rows > n_ridx >= 0 <= n_cidx < cols:
                    nz_idx = (n_ridx * cols) + n_cidx
                    next_config_list[z_idx], next_config_list[nz_idx] = next_config_list[nz_idx], next_config_list[z_idx]
                    next_config = (''.join(next_config_list), nz_idx)
                    if next_config not in configs_seen:

                        board_states.append(next_config)
                        configs_seen.add(next_config)
        steps += 1



print(find_solution([[1,2,3],[5,4,0]]))
