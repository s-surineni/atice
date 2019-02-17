# https://practice.geeksforgeeks.org/problems/word-break-part-2/0
test_cases = int(input().strip())
words = None

def break_words_util(big_string, res):
    # print('res', res)
    # print('big_string', big_string)
    for idx in range(1, len(big_string) + 1):  # + 1 because if only one element is
        # left, range(1, len('m')) returns empty list
        # print('currwrod', big_string[:idx])
        curr_str = big_string[:idx]
        if curr_str in words:
            res += ' ' + curr_str
            
            if idx == len(big_string):
                print(res)
                return
            break_words_util(big_string[idx:], res)


def break_words(big_string):
    return break_words_util(big_string, '')


for a_tc in range(test_cases):
    input()
    words = input().strip().split()
    # print(words)
    big_string = input().strip()
    break_words(big_string)
