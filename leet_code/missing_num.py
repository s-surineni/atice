def find_missing_num(num_list):
    tot = 0
    posit_len = 0
    num_len = len(num_list)
    for val in num_list:
        # tot += val if val > 0 else 0
        if val > 0:
            tot += val
            posit_len += 1

    first_num_sum = (num_len * (num_len + 1)) // 2
    return first_num_sum - tot


# print(find_missing_num([1, 4, 3, -1]))
print(find_missing_num([-2, -1]))
[1, 3, 4, -2, -2] len = 5, output = 2
[-4, -5, 52, 53]
