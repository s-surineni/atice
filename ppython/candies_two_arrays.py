ratings = [int(i) for i in input().split()]

rate_len = len(ratings)
ltr = [1] * rate_len
rtl = [1] * rate_len
candies = [1] * rate_len

for idx in range(1, rate_len):
    if ratings[idx - 1] < ratings[idx]:
        ltr[idx] = ltr[idx - 1] + 1

for idx in range((rate_len) - 2, -1, -1):
    if ratings[idx] > ratings[idx + 1]:
        rtl[idx] = rtl[idx + 1] + 1

for idx in range(rate_len):
    candies[idx] = max(rtl[idx], ltr[idx])
print(candies)
