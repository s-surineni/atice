def find_largest_divisible_set(nums):
    num_len = len(nums)
    nums = sorted(nums)
    dpc = []
    largest_idx, largest_size = (0, 1)
    for idx in range(num_len):
        dpc.append([idx, 1])
        for idx2 in range(idx):
            if nums[idx] % nums[idx2] == 0:
                divisors = 1 + dpc[idx2][1]
                if dpc[idx][1] < divisors:
                    dpc[idx][1] = divisors
                    dpc[idx][0] = idx2
                if largest_size < dpc[idx][1]:
                    largest_size = divisors
                    largest_idx = idx
    start_idx = largest_idx
    factors = []
    print(dpc)
    while start_idx != dpc[start_idx][0]:
        factors.append(nums[start_idx])
        start_idx = dpc[start_idx][0]
    factors.append(nums[start_idx])
    return factors


nums = [1, 2, 4, 8]
nums = [2, 4]

print(find_largest_divisible_set(nums))
