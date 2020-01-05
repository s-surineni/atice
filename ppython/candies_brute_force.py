# https://leetcode.com/problems/candy/


ratings = [int(i) for i in input().split()]
rate_len = len(ratings)
havent_updated_candies = False

candies = [1] * rate_len
# How is it working?
while not havent_updated_candies:
    havent_updated_candies = True
    for idx in range(rate_len):
        if idx > 0 and ratings[idx - 1] < ratings[idx] and candies[idx - 1] >= candies[idx]:
            candies[idx] = candies[idx - 1] + 1
            havent_updated_candies = False
        if idx < (rate_len - 1) and ratings[idx] > ratings[idx + 1] and candies[idx] <= candies[idx + 1]:
            candies[idx] = candies[idx + 1] + 1
            havent_updated_candies = False
    # print(candies)
print(candies)
