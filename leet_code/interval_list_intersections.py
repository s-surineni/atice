# https://leetcode.com/problems/interval-list-intersections
def find_list_intersections(list1, list2):
    idx1, idx2 = 0, 0
    res = []

    while idx1 < len(list1) and idx2 < len(list2):
        print(idx1, idx2)
        ll1, ll2 = list1[idx1], list2[idx2]
        lo = max(list1[idx1][0], list2[idx2][0])
        hi = min(list1[idx1][1], list2[idx2][1])
        if lo <= hi:
            res.append([lo, hi])
        # why only high are checked
        if ll1[1] < ll2[1]:
            idx1 += 1
        else:
            idx2 += 1
    return res


firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
print(find_list_intersections(firstList, secondList))
