def find_kids_with_greatest_candies(kid_candies, extra):
    max_can = max(kid_candies)

    for idx, can in enumerate(kid_candies):
        if can + extra >= max_can:
            kid_candies[idx] = True
        else:
            kid_candies[idx] = False

    return kid_candies


if __name__ == '__main__':
    print(find_kids_with_greatest_candies([2,3,5,1,3], 3))
