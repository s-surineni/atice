def find_smallest_range(num_list, val_range):
    min_val = min(num_list)
    max_val = max(num_list)
    mid_val = (min_val + max_val) // 2
    min_val = float('inf')
    max_val = -float('inf')
    for idx, val in enumerate(num_list):
        if val <= mid_val:
            num_list[idx] = (val + val_range
                             if (val + val_range) < mid_val else mid_val)
        else:
            num_list[idx] = (val - val_range if
                             (val - val_range) > mid_val else mid_val)

        if min_val > num_list[idx]:
            min_val = num_list[idx]
        if max_val < num_list[idx]:
            max_val = num_list[idx]

    return max_val - min_val


if __name__ == '__main__':
    print(find_smallest_range([1], 0))
    # print(find_smallest_range([0,10], 2))
    # print(find_smallest_range([1,3,6], 3))
