# https://leetcode.com/problems/range-addition-ii/
def find_max_integer(row, col, ops):
    mr, mc = None, None
    for ar, ac in ops:
        if not mr or ar < mr:
            mr = ar
        if not mc or ac < mc:
            mc = ac
    return mr * mc


m = 3
n = 3
ops = [[2, 2], [3, 3]]
print(find_max_integer(m, n, ops))
