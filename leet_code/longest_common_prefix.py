def find_longest_common_prefix(strs, start, end):
    if start >= end:
        return strs[start]
    elif len(strs) > 1:
        mid = (start + end) // 2
        res1 = find_longest_common_prefix(strs, start, mid)
        res2 = find_longest_common_prefix(strs, mid + 1, end)
    res1, res2 = (res1, res2) if len(res1) > len(res2) else (res2, res1)
    if not res2:
        return ""
    for idx in range(len(res2)):
        if res1[idx] != res2[idx]:
            break
    else:
        return res2
    return res1[:idx]


strs = ["flower", "flow", "flight"]
strs = ["", ""]
strs = ["ab", "a"]
print(find_longest_common_prefix(strs, 0, len(strs) - 1))
