paran_str = input('Please enter the parantheses: ')

stack = []


for par in paran_str:
    if par in '({[':
        stack.append(par)

    elif stack:
        open_par = stack.pop()

        if open_par == '(' and par != ')':
            print(paran_str, 'is invalid')
            break
        elif open_par == '[' and par != ']':
            print(paran_str, 'is invalid')
            break
        elif open_par == '{' and par != '}':
            print(paran_str, 'is invalid')
            break
    elif not stack:
        print(paran_str, 'is invalid')
        break
else:
    print(paran_str, 'is valid')
