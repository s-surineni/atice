from sys import maxsize


def merge(a_list, l, m, h):
    temp1 = [None] * (m - l + 2)
    temp2 = [None] * (h - m + 1)

    for idx in range(len(temp1) - 1):
        temp1[idx] = a_list[idx + l]
    
    temp1[len(temp1) - 1] = maxsize
    print('temp1', temp1)
    for idx in range(len(temp2) - 1):
        temp2[idx] = a_list[idx + m + 1]

    temp2[len(temp2) - 1] = maxsize
    print('temp2', temp2)
    id1 = id2 = 0

    for idx in range(l, h + 1):
        if temp1[id1] < temp2[id2]:
            a_list[idx] = temp1[id1]
            id1 += 1
        else:
            a_list[idx] = temp2[id2]
            id2 += 1
    print('a_list', a_list)
ip_list = [5, 2, 4, 6, 1, 3]

def merge_sort(a_list, lo, hi):
    if not lo < hi:
        return

    mi = (lo + hi) // 2
    merge_sort(a_list, lo, mi)
    merge_sort(a_list, mi + 1, hi)
    merge(a_list, lo, mi, hi)


merge_sort(ip_list, 0, len(ip_list) - 1)

print(ip_list)
