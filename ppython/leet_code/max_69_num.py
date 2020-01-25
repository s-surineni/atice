def parse_input():
    num = input('please enter the num: ')
    return num


def find_max(num):
    num_list = list(num)
    for idx, n in enumerate(num_list):
        if n == '6':
            num_list[idx] = '9'
            return ''.join(num_list)


# https://leetcode.com/problems/maximum-69-number/discuss/485738/Solution-for-Interview.-One-pass-without-convert-to-string
# above one doesn't convert num to string !.
num = parse_input()
print(find_max(num))
