def find_free_day():
    frns = int(input().strip())
    days = [0] * ((10**6) + 2)
    max_val = 0
    for _ in range(frns):
        pairs, *vals = [int(i) for i in input().strip().split()]
        # print(pairs, vals)
        for idx in range(0, len(vals), 2):
            st, ed = vals[idx], vals[idx + 1]
            max_val = max(max_val, ed)
            days[st] += 1
            days[ed + 1] -= 1
    cum_sum = 0
    idx = 1
    # Note: less than equal is necessary if we don't find any free days in the range
    # between 1 and max_date next value of max_date should be considered
    while idx <= max_val + 1:
        days[idx] += cum_sum
        cum_sum = days[idx]
        if not days[idx]:
            return idx
        idx += 1


print(find_free_day())
