# https://practice.geeksforgeeks.org/problems/convert-to-strictly-increasing-array/0
test_cases = int(input().strip())


def find_longest_increasing_subseq(ip_list):
    lis_len = [1] * len(ip_list)

    for idx in range(1, len(ip_list)):
        for idx2 in range(idx):
            if ip_list[idx] > ip_list[idx2] and lis_len[idx] < (lis_len[idx2] + 1):
                lis_len[idx] = lis_len[idx2] + 1
    return lis_len[len(ip_list) - 1]


for a_tc in range(test_cases):
    input()
    ip_list = input().strip().split()
    lis_len = find_longest_increasing_subseq(ip_list)
    print(len(ip_list) - lis_len)
