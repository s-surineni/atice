def find_minimum_add_to_make_paran_valid(parans):
    stack = []
    min_add = 0
    for par in parans:
        if par == '(':
            stack.append(par)
        else:
            if stack:
                stack.pop()
            else:
                min_add += 1
    min_add += len(stack)

    return min_add


print(find_minimum_add_to_make_paran_valid("())"))
print(find_minimum_add_to_make_paran_valid("()))(("))
