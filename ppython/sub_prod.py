# https://practice.geeksforgeeks.org/problems/count-the-subarrays-having-product-less-than-k/0
tcs = int(input().strip())
for trk in range(tcs):
    prod = int(input().strip().split()[1])
    ip_arr = input().strip().split()
    ip_arr = [int(i) for i in ip_arr]

    start = res = 0
    curr_prod = 1
    for end in range(len(ip_arr)):
        curr_prod *= ip_arr[end]

        while curr_prod >= prod and start < end:
            curr_prod //= ip_arr[start]
            start += 1

        if curr_prod < prod:
            res += end - start + 1
    print(res)
