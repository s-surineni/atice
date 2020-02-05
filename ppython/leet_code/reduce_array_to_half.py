def reduce_array_to_half(arr):
    orig_size = len(arr)
    unique_vals = set(arr)

    occur_count = {}
    for val in unique_vals:
        occurance = arr.count(val)
        if occur_count.get(occurance):
            occur_count[occurance].append(val)
        else:
            occur_count[occurance] = [val]

    sorted_occ = sorted(occur_count.keys())[::-1]

    curr_size = orig_size
    removed = 0

    while curr_size > orig_size // 2:
        max_now = sorted_occ[0]
        curr_size -= max_now
        
        # if not occur_count.get(max_now):
        #     sorted_occ.pop()
        # else:
        #     occur_count[max_now].pop()

        occur_count[max_now].pop()
        if not occur_count.get(max_now):
            sorted_occ.pop(0)

        removed += 1
    return removed


# arr = [3,3,3,3,5,5,5,2,2,7]
# arr = [1,9]
arr = [9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]
print(reduce_array_to_half(arr))
