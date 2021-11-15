# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/
from collections import Counter


def bit_mask(word):
    val = 0
    for ch in word:
        val |= 1 << ord(ch) - ord("a")
    return val


def find_num_valid_words_for_puzzle(words, puzzles):
    words = [bit_mask(a_word) for a_word in words]
    word_count = Counter(words)
    print(words)
    res = []
    for a_puzz in puzzles:
        first_char = 0 | 1 << (ord(a_puzz[0]) - ord("a"))
        mask = bit_mask(a_puzz[1:])
        sub_mask = mask
        # (ques?) wouldn't first appear again in while loop
        res.append(word_count[first_char])
        while sub_mask:
            res[-1] += word_count[(sub_mask) | first_char]
            # (ques?) how skpping over values (sub_mask) and not ant mask working
            sub_mask = (sub_mask - 1) & mask
            # print(sub_mask)
    return res


words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
print(find_num_valid_words_for_puzzle(words, puzzles))
