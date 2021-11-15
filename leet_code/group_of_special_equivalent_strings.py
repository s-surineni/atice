from collections import defaultdict


def find_max_group(str_arr):
    max_grp_size = 0
    groups = defaultdict(lambda: 0)
    for strn in str_arr:
        # instead of sorting we can use a list of 26 chars and compare those to
        # see if strings are equal
        sorted_strn = str(sorted(strn))
        groups[sorted_strn] += 1
        if groups[sorted_strn] > max_grp_size:
            max_grp_size = groups[sorted_strn]
    return max_grp_size


str_arr = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
print(find_max_group(str_arr))
