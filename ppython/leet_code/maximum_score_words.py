from collections import Counter


def calculate_word_score(word, letter_score):
    score = sum((letter_score[ord(c) - ord('a')] for c in word))
    print('word score', word, score)
    return score

def find_max_score_words_recur(words, rem_letters, score, curr_word, letter_score):
    if curr_word == len(words) or not rem_letters:
        return score
    score_ex = find_max_score_words_recur(words, rem_letters, score, curr_word + 1, letter_score)

    if not Counter(words[curr_word]) - rem_letters:
        score_ex = max(score_ex, find_max_score_words_recur(words,
                                              rem_letters - Counter(words[curr_word]),
                                              score + calculate_word_score(words[curr_word], letter_score),
                                              curr_word + 1,
                                              letter_score))
    return score_ex

def find_max_score_words(words, letters, score):
    return find_max_score_words_recur(words, Counter(letters), 0, 0, score)


words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

print(find_max_score_words(words, letters, score))
# print(find_max_score_words(["xxxz","ax","bx","cx"],
#                            ["z","a","b","c","x","x","x"],
#                            [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]))
