def backspace_string_compare(str1, str2):
    str1_idx = len(str1) - 1
    str2_idx = len(str2) - 1

    back_count1 = 0
    back_count2 = 0

    while True:
        while str1_idx >= 0 and (str1[str1_idx] == '#' or back_count1):
            back_count1 += 1 if str1[str1_idx] == '#' else -1
            str1_idx -= 1
        while str2_idx >= 0 and (str2[str2_idx] == '#' or back_count2):
            back_count2 += 1 if str2[str2_idx] == '#' else -1
            str2_idx -= 1
        if not (str1_idx >= 0 and str2_idx >= 0
                and str1[str1_idx] == str2[str2_idx]):
            return str1_idx == str2_idx == -1
        str1_idx, str2_idx = str1_idx - 1, str2_idx - 1


print(backspace_string_compare("y#fo##f", "y#f#o##f"))
