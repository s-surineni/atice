def find_best_time_to_buy(prices, trans):
    price_count = len(prices)
    cache = [[0] * price_count for _ in range(trans + 1)]
    for trans_val in range(1, trans + 1):
        min_val = prices[0]
        for today in range(1, price_count):
            min_val = min(min_val, prices[today] - cache[trans_val - 1][today - 1])
            cache[trans_val][today] = max(
                cache[trans_val][today - 1], prices[today] - min_val
            )

    return cache[trans_val][price_count - 1]
    print("*" * 80)
    print("ironman cache", cache)


prices = [3, 3, 5, 0, 0, 3, 1, 4]
# prices = [1, 2, 3, 4, 5]
prices = [int(i) for i in open("input.txt").read().split(",")]
trans = 2
print("*" * 80)
print("ironman find_best_time_to_buy", find_best_time_to_buy(prices, trans))
