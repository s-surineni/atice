ratings = [int(i) for i in input().split()]

rate_len = len(ratings)
ltr = [1] * rate_len
candies = [1] * rate_len

for idx in range(1, rate_len):
    if ratings[idx - 1] < ratings[idx]:
        candies[idx] = candies[idx - 1] + 1

for idx in range((rate_len) - 2, -1, -1):
    if ratings[idx] > ratings[idx + 1]:
        candies[idx] = candies[idx] if candies[idx] > candies[idx + 1] + 1 else candies[idx + 1] + 1


print(candies)
