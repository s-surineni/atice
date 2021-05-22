def find_if_score(tiles, hole, step):
    if not hole % step:
        return 'yes'
    elif (tiles + 1) % step == hole % step:
        return 'yes'
    else:
        return 'no'


test_cases = int(input().strip())

for a_tc in range(test_cases):
    inp = [int(i) for i in input().strip().split()]
    print(find_if_score(*inp))
