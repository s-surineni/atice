def find_solubility(deg, sol, fact):
    return (((100 - deg) * fact) + sol) * 10


test_cases = int(input().strip())

for a_tc in range(test_cases):
    inp = [int(i) for i in input().strip().split()]
    print(find_solubility(*inp))
