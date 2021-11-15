# https://practice.geeksforgeeks.org/problems/reversing-the-vowels/0
tcs = int(input().strip())

vows = 'aeiou'
for trk in range(tcs):
    a_str = input().strip()
    a_str = list(a_str)
    # print('a_str', a_str)
    left = 0
    right = len(a_str) - 1
    while left < right:
        while left < right:
            if a_str[left].casefold() not in vows:
                left += 1
            else:
                break
        # print('left', a_str[left])
        while left < right:
            if a_str[right].casefold() not in vows:
                right -= 1
            else:
                break
        # print('right', a_str[right])
        a_str[left], a_str[right] = a_str[right], a_str[left]
        left += 1
        right -= 1
    print(''.join(a_str))
