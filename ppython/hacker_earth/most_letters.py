from collections import Counter


def find_most_freq(strn):
    char_count = Counter(strn)
    return char_count.most_common()[0][-1]


ip = 'vrowrqt'
print(find_most_freq(ip))
