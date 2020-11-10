tc = int(input())
for _ in range(tc):
    input()
    b_arr = [int(i) for i in input().split()]
    b_len = len(b_arr)
    idx = b_len - 1
    val = 1
    while idx >= 0:
        if b_arr[idx] == idx + 1:
            b_arr[idx] = val
            val += 1
        else:
            b_arr[idx] = b_arr[b_arr[idx] - 1]
        idx -= 1
    for val in b_arr:
        print(val, end=' ')
