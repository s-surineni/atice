def find_r_comb_n_recur(elements, start, r, combinations, current_combi):
    if len(current_combi) == r:
        combinations.append(current_combi)
        return
    ele_count = len(elements)
    # idx = 0
    while (ele_count - start) >= r - len(current_combi):
        find_r_comb_n_recur(elements,
                            start + 1,
                            r,
                            combinations,
                            current_combi + [elements[start]])
        start += 1
    return combinations

def find_r_comb_n():
    print(find_r_comb_n_recur([0, 1, 2, 3, 4], 0, 3, [], []))


find_r_comb_n()
