# https://leetcode.com/problems/roman-to-integer/

def get_int_val_from_rom(roman_dig):
    if roman_dig == 'I':
        return 1
    elif roman_dig == 'V':
        return 5
    elif roman_dig == 'X':
        return 10
    elif roman_dig == 'L':
        return 50
    elif roman_dig == 'C':
        return 100
    elif roman_dig == 'D':
        return 500
    elif roman_dig == 'M':
        return 1000


def roman_to_int(roman_num):
    idx = 0
    total = 0
    while idx < (len(roman_num) - 1):
        curr_val = get_int_val_from_rom(roman_num[idx])
        next_val = get_int_val_from_rom(roman_num[idx + 1])

        if curr_val >= next_val:
            total += curr_val
        else:
            total -= curr_val
        idx += 1
    next_val = get_int_val_from_rom(roman_num[-1])
    total += next_val
    return total


if __name__ == '__main__':
    print(roman_to_int('III'))
    print(roman_to_int('IV'))
    print(roman_to_int("LVIII"))
