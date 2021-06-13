from collections import deque


def find_max_score(nums, wdow_len):
    num_count = len(nums)
    dp_cache = [None] * num_count
    dp_cache[-1] = nums[-1]
    window = deque()
    window.append(num_count - 1)

    for trk in range(num_count - 2, -1, -1):
        # while window and len(window) > wdow_len:
        #     window.popleft()

        if window[0] - trk > wdow_len:
            window.popleft()

        dp_cache[trk] = dp_cache[window[0]] + nums[trk]

        while window and dp_cache[window[-1]] <= dp_cache[trk]:
            window.pop()
        window.append(trk)

    return dp_cache[0]


nums = [1,-1,-2,4,-7,3]
k = 2
print(find_max_score(nums, k))