# https://leetcode.com/problems/arranging-coins/
import math


def arranging_coins(coins):
    steps = math.floor(math.sqrt((2 * coins) + 1 / 4) - (1 / 2))
    return steps


coins = 5
print(arranging_coins(coins))
