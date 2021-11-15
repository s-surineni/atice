test_cases = int(input().strip())

for a_tc in range(test_cases):
    expr = input().strip()
    stack = []
    br_count = 0
    for sym in expr:
        if sym == '(':
            br_count += 1
            print(br_count, end=' ')
            stack.append(br_count)
        elif sym == ')':
            print(stack.pop(), end=' ')
    print()
