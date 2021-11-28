# https://www.codechef.com/LTIME102C/problems/MINPIZZAS
def find_min_pizzas(friends, pieces):
    # no if friends are less than pieces
    if friends <= pieces:
        # friends not factor of pieces
        if pieces % friends == 0:
            return 1
        else:
            prod = 2
            while (pieces * prod) % friends:
                prod += 1
            return prod
    else:
        prod = 2
        while (pieces * prod) % friends:
            prod += 1
        return prod


def driver():
    tc = int(input().strip())
    for _ in range(tc):
        fr, pi = [int(i) for i in input().strip().split()]
        print(find_min_pizzas(fr, pi))


driver()
