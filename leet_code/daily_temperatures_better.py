# https://leetcode.com/problems/daily-temperatures/
def daily_temperatures(temps):
    stack = []
    res = [0] * len(temps)
    for idx, val in enumerate(temps):
        while stack and temps[stack[-1]] < val:
            prev_day = stack.pop()
            res[prev_day] = idx - prev_day
        stack.append(idx)
    return res


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
temperatures = [30, 40, 50, 60]
temperatures = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
print(daily_temperatures(temperatures))
