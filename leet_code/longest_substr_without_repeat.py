def find_max_non_rep_substr(s):
    st = 0
    ed = 0
    str_ch = set()
    max_size = 0
    curr_size = 0
    for idx, val in enumerate(s):
        print('str_ch', str_ch)
        if val in str_ch:
            if curr_size > max_size:
                max_size = curr_size
                
            for idx2, val2 in enumerate(s[st: ed + 1]):
                print(val, val2, 'vals')
                if val == val2:
                    st += (idx2 + 1)
                    # ed += 1
                    curr_size = len(str_ch)
                    break
                else:
                    str_ch.remove(val2)
        else:
            str_ch.add(val)
            curr_size += 1
            ed += 1
    if max_size < curr_size:
        max_size = curr_size
    return max_size


print(find_max_non_rep_substr("abcabcbb"))