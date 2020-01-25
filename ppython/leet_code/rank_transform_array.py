def parse_input():
    nums = [int(i) for i in input('Please enter numbers separated by commas: ').split(',')]
    return nums

def rank_transform(arr):
    vals_dict = {}
    for idx, val in enumerate(arr):
        if vals_dict.get(val):
            vals_dict[val].append(idx)
        else:
            vals_dict[val] = [idx]

    dup_arr = arr[:]
    dup_arr.sort()
    rank_arr = []
    curr_rank = 1
    prev_val = dup_arr[0]
    for val in dup_arr:
        if prev_val != val:
            curr_rank += 1
        vals_dict[val].append(curr_rank)

    for val in arr:
        rank_arr.append(vals_dict[val][-1])
    return rank_arr


arr = parse_input()
print(rank_transform(arr))
