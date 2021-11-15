tc = int(input().strip())
ranks = [int(i) for i in input().strip().split()]

merged = []

sign = 1 if ranks[0] >= 1 else -1
curr_sum = 0
for val in ranks:
    if val * sign > 0:
        curr_sum += val
    else:
        merged.append(curr_sum)
        curr_sum = val
        sign = - (sign)
merged.append(curr_sum)


max_three_sum = 0
for idx in range(len(merged)):
    three_sum = 0
    sum_count = 0
    while idx < len(merged) and sum_count < 3:
        three_sum += merged[idx]
        idx += 2
        sum_count += 1
    if abs(max_three_sum) < abs(three_sum):
        max_three_sum = abs(three_sum)

print(len(merged), max_three_sum)
