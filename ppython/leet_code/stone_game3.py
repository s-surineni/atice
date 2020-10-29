import sys


def find_stone_game_3_dp(stones, stone_loc, dp_holds):
    ans = -sys.maxsize
    stone_count = len(stones)

    if stone_loc >= stone_count:
        return 0


    if dp_holds[stone_loc] > -1:
        return dp_holds[stone_loc]

    ans = max(
        ans,
        stones[stone_loc] - find_stone_game_3_dp(stones, stone_loc + 1, dp_holds))
    if stone_loc + 1 < stone_count:
        ans = max(
            ans, stones[stone_loc] + stones[stone_loc + 1] -
            find_stone_game_3_dp(stones, stone_loc + 2, dp_holds))
    if stone_loc + 2 < stone_count:
        ans = max(
            ans,
            stones[stone_loc] + stones[stone_loc + 1] + stones[stone_loc + 2] -
            find_stone_game_3_dp(stones, stone_loc + 3, dp_holds))
    dp_holds[stone_loc] = ans
    return ans


def find_stone_game_3(stones):
    dp_holds = [-1] * len(stones)
    alice_score = find_stone_game_3_dp(stones, 0, dp_holds)
    if alice_score > 0:
        return 'Alice'
    if alice_score == 0:
        return 'Tie'
    return 'Bob'


stones = [1, 2, 3, 7]
# stones = [1, 2, 3, -9]
print(find_stone_game_3(stones))
