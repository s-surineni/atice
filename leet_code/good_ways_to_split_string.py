def find_good_way(strn):
    str_len = len(strn)
    forward = [0] * str_len
    backward = [0] * str_len
    uni = set()

    for idx, ele in enumerate(strn):
        uni.add(ele)
        forward[idx] = len(uni)

    uni = set()
    for idx in range(str_len - 1, -1, -1):
        backward[idx] = len(uni)
        uni.add(strn[idx])

    ways = 0
    for fw, bw in zip(forward, backward):
        if fw == bw:
            ways += 1
    return ways


# s = "aacaba"
# s = "abcd"
# s = "aaaaa"
# s = 'a'
s = "acbadbaada"
print(find_good_way(s))
