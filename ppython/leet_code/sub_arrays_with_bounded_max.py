# TODO do the brute force approach and see how all the combinations
# that occur in brute force are being captured in this approach
def find_num_subarray_with_bound_max(nums, le, ri):
    # Better here only one variable is used instead of storing all values in array
    cache, res = 0, 0
    # Better idea to get correct diff
    prev = -1
    # TODO: see what other situations this approach of finding all combinations can be used
    # calculating subarray's ending at i

    for trk, val in enumerate(nums):
        if val < le:
            # Notice the number of subarrays are not increasing here
            res += cache
        elif val > ri:
            cache = 0
            prev = trk
        else:
            cache = trk - prev
            res += cache
    return res


# nums = [2, 1, 4, 3]
# left = 2
# right = 3

nums = [876,880,482,260,132,421,732,703,795,420,871,445,400,291,358,589,617,202,755,810,227,813,549,791,418,528,835,401,526,584,873,662,13,314,988,101,299,816,833,224,160,852,179,769,646,558,661,808,651,982,878,918,406,551,467,87,139,387,16,531,307,389,939,551,613,36,528,460,404,314,66,111,458,531,944,461,951,419,82,896,467,353,704,905,705,760,61,422,395,298,127,516,153,299,801,341,668,598,98,241]
left = 658
right = 719

print(find_num_subarray_with_bound_max(nums, left, right))
