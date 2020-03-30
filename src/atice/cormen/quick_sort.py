def partition(num_list, st, ed):
    # if st >= ed:  as we are already checking in quick_sort_recur we need not have a condition here <!notes>
    #     return 
    piv_ele = num_list[ed]
    i = st - 1
    for idx in range(st, ed):
        if num_list[idx] < piv_ele:
            i += 1
            num_list[i], num_list[idx] = num_list[idx], num_list[i]
    i += 1
    num_list[i], num_list[ed] = num_list[ed], num_list[i]
    return i

def quick_sort_recur(num_list, st, ed):
    # if st < ed: then do rest was also a possibility
    if st >= ed:
        return
    piv = partition(num_list, st, ed)
    # if piv is None: return
    quick_sort_recur(num_list, st, piv - 1)
    quick_sort_recur(num_list, piv + 1, ed)


num_list = [1, 5, 2, 4, 3]
quick_sort_recur(num_list, 0, len(num_list) - 1)
print(num_list)
