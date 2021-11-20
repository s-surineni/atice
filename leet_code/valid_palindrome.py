def isPalindrome(s):
    ft = 0
    bk = len(s) - 1
    while ft < bk:
        while (
            not (ord("A") <= ord(s[ft]) <= ord("Z"))
            and not (ord("a") <= ord(s[ft]) <= ord("z"))
            and ft < bk
            and not (ord("0") <= ord(s[ft]) <= ord("9"))
        ):
            ft += 1
        while (
            not (ord("A") <= ord(s[bk]) <= ord("Z"))
            and not (ord("a") <= ord(s[bk]) <= ord("z"))
            and ft < bk
            and not (ord("0") <= ord(s[bk]) <= ord("9"))
        ):
            bk -= 1
        if ft > bk:
            return True
        if s[ft].casefold() != s[bk].casefold():
            return False
        ft += 1
        bk -= 1
    return True


s = "A man, a plan, a canal: Panama"
# s = "0P"
# s = "ab2a"
# s = "ab_a"
print(isPalindrome(s))
