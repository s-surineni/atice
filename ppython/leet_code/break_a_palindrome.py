def parse_input():
    palindrome = input('Please enter a palindrome: ')
    return palindrome


def break_palindrome(palindrome):
    if len(palindrome) == 1:
        return ''
    pal_list = list(palindrome)

    for idx, ch in enumerate(pal_list):
        if ch != 'a' and idx != (len(palindrome) // 2):
            pal_list[idx] = 'a'
            break
    else:
        pal_list[-1] = 'b'
    return ''.join(pal_list)

palindrome = parse_input()
print(break_palindrome(palindrome))
