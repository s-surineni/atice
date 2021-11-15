def remove_outermost_paran(parans):
    res_paran, curr_p = [], 0
    for ch in parans:
        if ch == '(' and curr_p > 0:
            res_paran.append('(')
        elif ch == ')' and curr_p > 1:
            res_paran.append(')')
        if ch == '(':
            curr_p += 1
        else:
            curr_p -= 1
    return ''.join(res_paran)


print(remove_outermost_paran("(()())(())"))
