test_cases = int(input().strip())

for a_tc in range(test_cases):
    count, prod = input().strip().split()
    num_list = input().strip().split()
    num_list = [int(i) for i in num_list]
    prod = int(prod)

    start = end = 0
    curr_prod = 1
    sub_arr_count = 0
    while end < len(num_list):
        curr_prod *= num_list[end]
        while start < end and curr_prod >= prod:
            curr_prod //= num_list[start]
            start += 1
        # I have know idea how below statement is able
        # to calculate total sub_arrays
        if curr_prod < prod:
            sub_arr_count += (end - start + 1)
        # print(num_list[start:end + 1])
        end += 1
    print(sub_arr_count)
