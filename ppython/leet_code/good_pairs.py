# https://leetcode.com/problems/number-of-good-pairs/
from collections import Counter
from itertools import combinations





print(find_good_pairs([1, 2, 3, 1, 1, 3]))
print(find_good_pairs([1, 1, 1, 1]))
print(find_good_pairs([1,2,3]))
print(
    find_good_pairs([
        3, 1, 10, 2, 4, 8, 3, 2, 9, 5, 4, 8, 4, 3, 1, 5, 5, 7, 2, 2, 8, 8, 10,
        1, 7, 10, 5, 10, 2, 9, 8, 7, 10, 3, 10, 10, 9, 8, 10, 7, 3, 10, 2, 9,
        8, 3, 1, 2, 1, 6, 4, 9, 7, 5, 6, 7, 4, 5, 3, 1, 4, 2, 2, 1, 10, 4, 2,
        7, 3, 6, 5, 7, 3, 10
    ]))
