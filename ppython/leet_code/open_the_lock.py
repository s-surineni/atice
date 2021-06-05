from collections import deque


def find_successors(combi):
    neighbors = []
    for idx, ch in enumerate(combi):
        neighbors.append(combi[:idx] + str((int(ch) + 1) % 10) + combi[idx + 1]:)
        neighbors.append(combi[:idx] + str((int(ch) - 1) % 10) + combi[idx + 1]:)
    return neighbors

def open_the_lock(dead_end, target):
    dead_end = set(dead_end)
    qu = deque.append('0000')

    depth = -1

    while qu:
        depth += 1
        size = len(qu)
        combi = qu.popleft()
        for _ in range(size):
            if combi in dead_end:
                continue
            elif combi == target:
                return depth
            dead_end.add(combi)
            qu.extend(find_successors(combi))
    return -1
