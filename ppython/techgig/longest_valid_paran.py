paran_str = input()

stack = []

valid_len = 0
curr_len = 0
for par in paran_str:
    if par == '(':
        stack.append('(')
    elif stack and stack.pop() == '(':
        curr_len += 2
    elif curr_len > valid_len:
        valid_len = curr_len
        curr_len = 0
if curr_len > valid_len:
    valid_len = curr_len

print(valid_len)
