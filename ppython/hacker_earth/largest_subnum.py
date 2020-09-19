def find_larget_subnumber(str_len, divisor, strn):
    largest_xor = -1
    largest_num = -1
    curr_xor = int(strn[0])
    for idx in range(1, str_len - 1):
        int_val = int(strn[idx])

        # num should not start with 0
        if (int(strn[idx])) and (int(strn[idx:]) % divisor == 0) and (curr_xor > largest_xor):
            largest_xor = curr_xor
            largest_num = strn[idx:]
        curr_xor ^= int_val
    return largest_num


print(find_larget_subnumber(6, 2, '611234'))