def find_greater_than_this(num_list):
    greater_count = [0] * len(num_list)

    for idx in range(len(num_list) - 2, -1, -1):
        if num_list[idx] > num_list[idx + 1]:
            greater_count[idx] = greater_count[idx + 1] + 1
        else:
            for idx2 in range(idx +1 , len(num_list)):
                if num_list[idx] > num_list[idx2]:
                    greater_count[idx] = greater_count[idx2] + 1
                    break

    return greater_count




print(find_greater_than_this([4, 2, 3, 1, 5]))
