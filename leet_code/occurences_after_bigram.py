def find_occurences_after_bigram(text, first, second):
    word_list = text.split()
    total_words = len(word_list)
    result = []

    idx = 0
    while idx < total_words:
        if (word_list[idx] == first and word_list[idx + 1] == second
                and (idx + 2) < total_words):
            result.append(word_list[idx + 2])
            idx += 2
        else:
            idx += 1
    return result


if __name__ == '__main__':
    text = "alice is a good girl she is a good student"
    first = "a"
    second = "good"
    print(find_occurences_after_bigram(text, first, second))
