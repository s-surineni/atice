def find_all_dups_without_extra_space(num_list):
    num_list_len = len(num_list)
    for num in num_list:
        num = abs(num)

        if num > num_list_len:
            num = num - num_list_len
        if num_list[num - 1] > 0:
            num_list[num - 1] = - num_list[num - 1]
        else:
            num_list[num - 1] += ((-2 * num_list[num - 1]) + num_list_len)

    dup_list = []

    for idx, val in enumerate(num_list):
        if val > num_list_len:
            dup_list.append(idx + 1)
    return dup_list


num_list = [10,2,5,10,9,1,1,4,3,7]
# num_list = [4,3,2,7,8,2,3,1]
print(find_all_dups_without_extra_space(num_list))
