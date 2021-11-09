# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/
def find_valid_words(words, puzzle):
    res = []
    for a_puzz in puzzle:
        first_char = a_puzz[0]
        puzzle = set(a_puzz)
        res.append(0)
        for idx, a_word in enumerate(words):
            a_word = set(a_word)
            if first_char in a_word and a_word < puzzle:
                res[-1] += 1
    return res


words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
print(find_valid_words(words, puzzles))
