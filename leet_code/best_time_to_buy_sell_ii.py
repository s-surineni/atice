# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
def best_time_to_buy_sell(prices):
    max_profit = 0
    for idx in range(len(prices) - 1):
        if prices[idx] < prices[idx + 1]:
            max_profit += prices[idx + 1] - prices[idx]
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(best_time_to_buy_sell(prices))
