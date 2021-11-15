from collections import Counter


def find_words_chars(words, chars):
    char_count = Counter(chars)
    len_sum = 0
    for a_word in words:
        a_word_counter = Counter(a_word)
        len_sum += len(
            a_word) if a_word_counter & char_count == a_word_counter else 0
    return len_sum


words = ["cat", "bt", "hat", "tree"]
chars = "atach"
print(find_words_chars(words, chars))
