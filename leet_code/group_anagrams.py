# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict


def group_anagrams(strs):
    anag = defaultdict(list)

    for st in strs:
        sortst = tuple(sorted(st))
        anag[sortst].append(st)
    print(anag)

    return list(anag.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))
