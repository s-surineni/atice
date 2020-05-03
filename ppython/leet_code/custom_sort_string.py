from collections import Counter


def custom_sort_string(str1, str2):
    str2_chars = Counter(str2)
    sorted_str2 = []

    for ch in str1:
        if ch in str2_chars:
            sorted_str2.extend([ch] * str2_chars[ch])
            del str2_chars[ch]

    for ch in str2_chars:
        sorted_str2.extend([ch] * str2_chars[ch])

    return ''.join(sorted_str2)


S = "cba"
T = "abcd"
print(custom_sort_string(S, T))
