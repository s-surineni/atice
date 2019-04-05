# https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

test_cases = int(input().strip())

for a_tc in range(test_cases):
    ip_str = input()
    c_idx = 0
    char_to_del = 0
    while c_idx < (len(ip_str) - 1):
        if ip_str[c_idx] == ip_str[c_idx + 1]:
            char_to_del += 1
        c_idx += 1
    print(char_to_del)
