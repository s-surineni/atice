def find_path_in_zigzag_recur(label, level, end, path):
    curr_start = end + 1
    curr_end = (2 ** (level - 1)) + end
    if curr_end >= label:
        path.append(label)
        return (curr_start + curr_end - label) // 2
    stop = find_path_in_zigzag_recur(label, level + 1,
                                       curr_end, path)
    path.append(stop)
    return (curr_start + curr_end - stop) // 2


def find_path_in_zigzag(label):
    if label == 1:
        return [1]
    path = []
    find_path_in_zigzag_recur(label, 2, 1, path)
    path.append(1)
    return path[::-1]


# print(find_path_in_zigzag(14))
# print(find_path_in_zigzag(26))
print(find_path_in_zigzag(3))
