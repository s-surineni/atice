# https://practice.geeksforgeeks.org/problems/most-frequent-word-in-an-array-of-strings/0
test_cases = int(input().strip())

for a_tc in range(test_cases):
    str_cnt = (input())
    str_list = input().strip().split()
    str_list.sort()
    str_cnt = {}
    max_c, max_w = 0, ''
    for a_str in str_list:
        if a_str in str_cnt:
            str_cnt[a_str] += 1
            if max_c < str_cnt[a_str]:
                max_c = str_cnt[a_str]
                max_w = a_str
        else:
            str_cnt[a_str] = 1
            
    # print(str_cnt)
    print(max_w)
    # print(max_c)
    # print(str_list)
