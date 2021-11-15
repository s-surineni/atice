def find_num_patches(nums, tar):
    miss = 1
    trk = 0
    added = 0
    while trk < len(nums):
        if trk < len(nums) and nums[trk] <= miss:
            miss += nums[trk]
            trk += 1
        else:
            miss += miss
            added += 1
    return added


nums = [1, 3]
n = 6

nums = [1,5,10]
n = 20
print(find_num_patches(nums, n))
