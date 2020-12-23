# https://leetcode.com/problems/task-scheduler/
from collections import Counter


def find_cpu_cycles(tasks, n):
    task_count = Counter(tasks)
    max_freq = max([v for v in task_count.values()])
    max_freq_count = [v for v in task_count.values()].count(max_freq)
    # print('*' * 80)
    # print('iron man max_freq, max_freq_count', max_freq, max_freq_count)
    part = max_freq - 1
    # blanks = (part * n) - ((max_freq_count - 1) * n)
    blanks = part * (n - (max_freq_count - 1))
    available_tasks = len(tasks) - max_freq * max_freq_count
    idles = max(0, blanks - available_tasks)
    return len(tasks) + idles



tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(find_cpu_cycles(tasks, n))
