# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
from collections import deque


def find_shortest_path_with_obstacle_removal(grid, k):
    que = deque([(0, 0, k)])
    lent = len(grid)
    bred = len(grid[0])

    if k > lent + bred - 2:
        return lent + bred - 2
    visited = set(
        (0, 0, k),
    )

    steps = 0
    wall = 1
    next_wall = 0
    while que:
        # print(que)
        while (
            wall
        ):  # (Notice) another way to keep track of steps is to add steps as extra value to store in queue Ex: que.append(x, y, rem, steps + 1)
            # val = que.popleft()
            # print("*" * 80)
            # print("ironman val", val)
            x, y, rem_obs = que.popleft()
            wall -= 1
            if x == lent - 1 and y == bred - 1:
                return steps
            visited.add((x, y, rem_obs))
            for x, y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if x < 0 or y < 0 or x >= lent or y >= bred:
                    continue
                if grid[x][y] and rem_obs:  # if grid[x,y] == 1 and rem_obs > 0
                    curr_step = (x, y, rem_obs - 1)
                    if curr_step not in visited:
                        visited.add(
                            curr_step
                        )  # (Notice) if visited is not added here there is a risk that same node is added multiple times in queue
                        que.append(curr_step)
                        next_wall += 1
                if not grid[x][y]:
                    curr_step = (x, y, rem_obs)
                    if curr_step not in visited:
                        # curr_step = (x, y, rem_obs)
                        visited.add(curr_step)
                        que.append(curr_step)
                        next_wall += 1

        wall = next_wall
        next_wall = 0
        steps += 1
    return -1
    # return steps
    # print("*" * 80)
    # print("ironman que", que)


# grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
# k = 1

# grid = [
#     [
#         0,
#         0,
#     ],
#     [0, 0],
#     [0, 0],
# ]
# k = 1

# grid = [[0, 1, 1], [1, 1, 1], [1, 0, 0]]
# k = 1
# grid = [[0, 1], [1, 1]]
# k = 0


grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
k = 1
print("*" * 80)
print(
    "ironman find_shortest_path_with_obstacle_removal(grid, k)",
    find_shortest_path_with_obstacle_removal(grid, k),
)
