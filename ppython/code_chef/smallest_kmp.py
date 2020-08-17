from collections import Counter
import sys

tc = int(input().strip())

for _ in range(tc):
    strn = input()
    pattern = input()

    strnd = Counter(strn)
    patd = Counter(pattern)

    res = strnd - patd
    # print('*' * 80)
    # print('iron man res', res)
    sort_keys = sorted(list(res.keys()))
    ress = []

    left = []
    right = []
    idx = 0
    for idx, ch in enumerate(sort_keys):
        if ch < pattern[0]:
            left += ch * res[ch]
        else:
            break
    else:
        print(''.join(left) + pattern)
        sys.exit()
    if pattern[0] > pattern[1]:
        print(''.join(left) + pattern + ''.join([ch * res[ch] for ch in sort_keys[idx:]]))
    else:
        if sort_keys[idx] == pattern[0]:
            ch = sort_keys[idx]
            left += ch * res[ch]
            idx += 1
        print(''.join(left) + pattern + ''.join([ch * res[ch] for ch in sort_keys[idx:]]))
    # print('*' * 80)
    # print('iron man left, right', left, right)
    # print(''.join(left) + pattern + ''.join(right))
