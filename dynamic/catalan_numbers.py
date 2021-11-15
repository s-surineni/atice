def find_n_catalan_numbers(n):
    cat_cache = [0] * n
    cat_cache[0], cat_cache[1] = 1, 1

    for val in range(2, n):
        for val2 in range(val):
            cat_cache[val] += cat_cache[val2] * cat_cache[val - val2 - 1]
    return cat_cache



print(find_n_catalan_numbers(8))
