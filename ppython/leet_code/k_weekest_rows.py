def find_k_weakest_rows(mat, k):
    one_count = {}

    for idx, row in enumerate(mat):
        row_1_count = row.count(1)
        if one_count.get(row_1_count):
            one_count[row_1_count].append(idx)
        else:
            one_count[row_1_count] = [idx]
    # print(one_count)
    min_1s = sorted(one_count.keys())
    curr_min = 0
    row_resp = []
    while k > 0:
        curr_min_row = one_count[min_1s[curr_min]]
        while curr_min_row and k > 0:
            row_resp.append(curr_min_row.pop(0))
            k -= 1
        curr_min += 1
    return row_resp


mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]

k = 3


print(find_k_weakest_rows(mat, k))
