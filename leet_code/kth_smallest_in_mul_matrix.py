# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/


def find_kth_larget(rc, cc, kth):
    def enough(mid):
        count = 0
        for rid in range(1, rc + 1):
            # (Notice) see the num values less than mid == mid // rid
            count += min(mid // rid, cc)
        if count < kth:
            return False
        else:
            return True

    lo, hi = 1, rc * cc
    while lo < hi:
        mid = (lo + hi) // 2
        if enough(mid):
            hi = mid
        else:
            lo = mid + 1
    # (ques?) why the values is in lo instead of mid
    # how are we guaranteed what the lo value that is calculated exists in matrix
    return lo


m = 2
n = 3
k = 6
print(find_kth_larget(m, n, k))
