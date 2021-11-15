# https://leetcode.com/problems/daily-temperatures/
def daily_temperatures(temps):
    stack = []
    res = [0] * len(temps)
    for idx in range(len(temps) - 1):
        if temps[idx] >= temps[idx + 1]:
            stack.append(idx)
        else:
            res[idx] = 1
            while stack and temps[stack[-1]] < temps[idx + 1]:
                idx2 = stack.pop()
                res[idx2] = (idx + 1) - idx2
    return res


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
temperatures = [30, 40, 50, 60]
temperatures = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
print(daily_temperatures(temperatures))
