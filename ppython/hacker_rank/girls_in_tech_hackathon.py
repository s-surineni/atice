import sys


def find_group_to_start_with(groups):
    group_len = len(groups)
    bounds = []
    for idx, ti in enumerate(groups):
        current_bound = [None, None]
        left_side_upper_bound = idx - ti
        if left_side_upper_bound >= 0:
            current_bound[0] = [0, left_side_upper_bound]
        right_side_upper_bound = idx + group_len - ti
        if right_side_upper_bound < group_len:
            current_bound[1] = [(idx + 1) % group_len, (right_side_upper_bound) % group_len]
        bounds.append(current_bound)
    print(bounds)
    sum_arr = [0] * group_len
    for a_bo in bounds:
        try:
            lb, ub = a_bo
            if lb:
                lo, hi = lb
                sum_arr[lo] += 1
                sum_arr[hi + 1] -= 1
            if ub:
                lo, hi = ub
                sum_arr[lo] += 1
                sum_arr[hi + 1] -= 1
        except:
            pass

    max_val = sum_arr[0]
    max_idx = 0
    for idx in range(1, group_len):
        sum_arr[idx] += sum_arr[idx - 1]
        if max_val < sum_arr[idx]:
            max_val = sum_arr[idx]
            max_idx = idx
    print('*' * 80)
    print('iron man sum_arr', sum_arr)
    return max_idx


# sample = [3, 1, 2, 1]
# print('sample', sample)
# print(find_group_to_start_with(sample))


# sample = [0, 1, 2, 3]
# print('sample', sample)
# print(find_group_to_start_with(sample))


# sample = [3, 0, 1, 2]
# print('sample', sample)
# print(find_group_to_start_with(sample))

# sample = [2, 3, 0, 1]
# print('sample', sample)
# print(find_group_to_start_with(sample))

# sample = [1, 1, 1, 1]
# print('sample', sample)
# print(find_group_to_start_with(sample))


sample = [1, 0, 1, 1]
print('sample', sample)
print(find_group_to_start_with(sample))