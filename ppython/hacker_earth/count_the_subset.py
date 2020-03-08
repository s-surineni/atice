def find_all_combinations_recur(arr, start, end, indx, set_len, curr_comb, all_comb):
    print('all', all_comb)
    print('current', curr_comb)
    if indx == set_len:
        all_comb.append(curr_comb)
        return
    idx = start
    while(idx <= end and end - idx + 1 >= set_len - indx):
        # curr_comb.append(idx)
        find_all_combinations_recur(arr, idx + 1, end, indx + 1, set_len, curr_comb + [idx], all_comb)
        idx += 1
    return all_comb
def find_all_combinations(set_sizes, arr_len, set_len):
    all_combs = find_all_combinations_recur(set_sizes, 0, arr_len - 1, 0, set_len, [], [])
    print(all_combs)
    
def count_subset(set_sizes, set_len, arr_len):
    combinations = find_all_combinations(set_sizes, arr_len, set_len)
    
    
tc = 1
# arr_len, set_len = [int(i) for i in input().split()]
# set_sizes = [int(i) for i in input().split()]

for _ in range(tc):
    # count_subset(set_sizes, set_len, arr_len)
    count_subset([1, 1, 2, 1], 3, 4)
