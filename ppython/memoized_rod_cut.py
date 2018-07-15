length_price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def memoized_cut_rod_aux(length, length_price, max_revenues):
    # print('length', length)
    curr_revenue = -1
    if max_revenues[length - 1] > 0:
        return max_revenues[length - 1]
    elif length == 0:
        curr_revenue = 0
    else:
        for trk in range(length):
            curr_revenue = max(curr_revenue, length_price[trk] +
                               memoized_cut_rod_aux(length - trk - 1,
                                                    length_price,
                                                    max_revenues))
        max_revenues[length - 1] = curr_revenue
    return curr_revenue


def memoized_cut_rod(length, length_price):
    max_revenues = [-1] * length
    memoized_cut_rod_aux(length, length_price, max_revenues)
    print(max_revenues)


length = int(input('Please enter a length to computer the values: '))
memoized_cut_rod(length, length_price)
