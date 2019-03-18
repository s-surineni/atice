# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/anagrams-651/description/


test_cases = int(input().strip())

for a_tc in range(test_cases):
    s1 = input()
    s2 = input()
    d1 = {}
    d2 = {}
    # print('s1', s1)
    # print('s2', s2)
    for ch in s1:
        if ch in d1:
            d1[ch] += 1
        else:
            d1[ch] = 1

    for ch in s2:
        if ch in d2:
            d2[ch] += 1
        else:
            d2[ch] = 1
    # print('d1', d1)
    # print('d2', d2)
    char_to_change = 0
    for key in d1:
        curr_char_count = d1[key]
        if key in d2:
            curr_char_count -= d2[key]
            curr_char_count = abs(curr_char_count)
            d2[key] = 0
        char_to_change += curr_char_count
    for key in d2:
        char_to_change += d2[key]

    print(abs(char_to_change))
