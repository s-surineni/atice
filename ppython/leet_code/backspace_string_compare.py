def backspace_string_compare(str1, str2):
    str_list1 = []
    last_idx1 = -1
    for ch in str1:
        if ch == '#':
            if last_idx1 > -1:
                last_idx1 -= 1
        else:
            if last_idx1 == (len(str_list1) - 1):
                str_list1.append(ch)
                last_idx1 += 1
            else:
                last_idx1 += 1
                str_list1[last_idx1] = ch

    str_list2 = []
    last_idx2 = -1
    for ch in str2:
        if ch == '#':
            if last_idx2 > -1:
                last_idx2 -= 1
        else:
            if last_idx2 == (len(str_list2) - 1):
                str_list2.append(ch)
                last_idx2 += 1
            else:
                last_idx2 += 1
                str_list2[last_idx2] = ch

    if last_idx1 != last_idx2:
        return False
    for idx in range(last_idx1 + 1):
        if str_list1[idx] != str_list2[idx]:
            return False
    return True


print(backspace_string_compare("y#fo##f", "y#f#o##f"))
