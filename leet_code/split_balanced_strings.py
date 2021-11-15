def parse_input():
    ex_str = input('Please enter a string: ')
    return ex_str

def split_balanced_string(ex_str):
    bal = 0
    tot = 0
    for ch in ex_str:
        bal += 1 if ch == 'R' else -1
        if bal == 0:
            tot += 1
    return tot


ex_str = parse_input()
print(split_balanced_string(ex_str))
