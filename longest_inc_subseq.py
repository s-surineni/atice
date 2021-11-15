def longest_inc_subseq(num_list):
    len_list = [1] * len(num_list)

    max_val = 0
    for idx1 in range(1, len(num_list)):
        for idx2 in range(idx1):
            if (num_list[idx1] > num_list[idx2] and
                len_list[idx1]  < len_list[idx2] + 1):
                len_list[idx1] = len_list[idx2] + 1
        max_val = max(max_val, len_list[idx1])
    return max_val

if __name__ == '__main__':
    print(longest_inc_subseq([10, 22, 9, 33, 21, 50, 41, 60]))
