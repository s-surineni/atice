from collections import Counter


def find_largest_string(strn):
    str_counter = Counter(strn)
    sorted_keys = sorted(str_counter.keys(), reverse=True)
    last_seen = None
    res = ''
    while True:
        for ke in sorted_keys:
            if str_counter[ke] and last_seen != ke:
                last_seen = ke
                reps = min(str_counter[ke], 2)
                res += reps * ke
                str_counter[ke] -= reps
                break
            print(str_counter)
        else:
            break
    return res


print(find_largest_string('baccc'))
print(find_largest_string('zzzazz'))
