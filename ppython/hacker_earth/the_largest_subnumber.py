def find_larget_subnumber(str_len, divisor, strn):
    largest_xor = 0
    largest_num = 0
    curr_xor = 0
    for idx in range(str_len - 1):
        int_val = int(strn[idx])
        curr_xor ^= int_val
        # num should not start with 0
        if not int(strn[idx + 1]):
            continue
        if not int(strn[idx + 1:]) % divisor:
            if curr_xor > largest_xor:
                largest_xor = curr_xor
                largest_num = strn[idx + 1:]
    return largest_num if largest_num else -1


print(find_larget_subnumber(6, 2, '611234'))
# print(find_larget_subnumber(6, 2, '610234'))
