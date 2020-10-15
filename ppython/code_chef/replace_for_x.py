# https://www.codechef.com/OCT20B/problems/REPLESX

test_cases = int(input().strip())

for a_tc in range(test_cases):
    _, tar, p, k = [int(i) for i in input().strip().split()]
    p, k = (p, k) if p < k else (k, p)
    all_nums = [int(i) for i in input().strip().split()]
    all_nums.sort()
    if tar > all_nums[k - 1] or tar > all_nums[p - 1]:
        print(-1)
    else:
        print(1)
