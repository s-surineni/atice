def find_ways_to_decode(numstr):
    if not numstr:
        return 0
    lent = len(numstr)
    dp = [0] * (lent + 1)

    # base case initialization
    dp[0] = 1
    dp[1] = 0 if numstr[0] == "0" else 1

    for i in range(2, len(numstr) + 1):
        # One step jump
        if 0 < int(numstr[i - 1]) <= 9:
            dp[i] += dp[i - 1]
        # Two step jump
        if 10 <= int(numstr[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]
    return dp[-1]


# print(numDecodings("231"))
# print(numDecodings("123"))
# print(numDecodings("1234"))
# print(numDecodings("1221"))
# print(find_ways_to_decode("3333"))
print(find_ways_to_decode("032"))
