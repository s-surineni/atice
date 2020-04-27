def backspace_string_compare(str1):
    stck1 = []
    for ch in str1:
        # <!note> this was better because
        # we checked negative case
        if ch != '#':
            stck1.append(ch)
        elif stck1:
            stck1.pop()
    return stck1

str1 = "y#fo##f"
str2 = "y#f#o##f"
print(backspace_string_compare(str1))
print(backspace_string_compare(str2))
