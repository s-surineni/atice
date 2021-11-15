# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/anagrams-651/description/


test_cases = int(input().strip())

for a_tc in range(test_cases):
    s1 = input()
    s2 = input()
    chars = [0] * 26
    for ch in s1:
        chars[ord(ch) - ord('a')] += 1
        
    for ch in s2:
        chars[ord(ch) - ord('a')] -= 1
    
    # print('d1', d1)
    # print('d2', d2)
    char_to_change = 0
    for freq in chars:
        char_to_change += abs(freq)
    
    print((char_to_change))
