def find_lexicographically_smallest_string(compstr):
    compstr += '<'
    res = ''
    strlen = len(compstr)
    curr_idx = 0
    while curr_idx < strlen:
        curr_comp = compstr[curr_idx]
        if curr_comp == '<':
            res += chr(ord('a') + curr_idx)
            curr_idx += 1
        else:
            rev_start = curr_idx
            incr_len = 1
            curr_idx += 1
            while compstr[curr_idx] == '>':
                incr_len += 1
                curr_idx += 1
            rev_idx = curr_idx
            # <!better> because instead of reversing string we are just
            # forming string in a reverse way
            while rev_start <= rev_idx:
                res += chr(ord('a') + rev_idx)
                rev_idx -= 1
            curr_idx += 1

    return res


# compstr = '<>'
# compstr = '><'
compstr = '<><'

print(find_lexicographically_smallest_string(compstr))
