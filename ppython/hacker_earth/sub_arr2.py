def find_fwd_len(arr):
    arlen = len(arr)
    len_arr = [1] * arlen
    great_stack = []
    for idx, val in enumerate(arr):
        if great_stack:
            while great_stack and arr[great_stack[-1]] < val:
                less_idx = great_stack.pop()
                len_arr[less_idx] = idx - less_idx

            great_stack.append(idx)
        else:
            great_stack.append(idx)
    for idx, val in enumerate(great_stack):
        len_arr[val] = arlen - val
    return len_arr

def find_bwd_len(arr):
    arlen = len(arr)
    len_arr = [1] * arlen
    great_stack = []
    for idx in range(arlen - 1, -1, -1):
        val = arr[idx]
        if great_stack:
            while great_stack and arr[great_stack[-1]] < val:
                less_idx = great_stack.pop()
                len_arr[less_idx] = abs(idx - less_idx)

            great_stack.append(idx)
        else:
            great_stack.append(idx)
    for idx, val in enumerate(great_stack):
        len_arr[val] = val + 1
    return len_arr

def find_sub_arry_len():
    arlen, queries = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    # print(arr)

    fwd_len = find_fwd_len(arr)
    # print(fwd_len)
    bwd_len = find_bwd_len(arr)
    # print(bwd_len)

    for _ in range(queries):
        sub_sum = 0
        st, ed = [int(i) for i in input().split()]
        for idx in range(st - 1, ed):
            n_val = fwd_len[idx] + bwd_len[idx] - 1
            sub_sum += (n_val * (n_val + 1)) // 2
        print(sub_sum)

find_sub_arry_len()
