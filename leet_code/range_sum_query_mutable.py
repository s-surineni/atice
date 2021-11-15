def build_segment_tree(nums):
    seg_tree = [0] * len(nums) * 2
    num_len = len(nums)

    for trk in range(num_len, 2 * num_len):
        seg_tree[trk] = nums[trk - num_len]
    for trk in range(num_len - 1, 0, -1):
        seg_tree[trk] = seg_tree[2 * trk] + seg_tree[2 * trk + 1]
    return seg_tree

class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.segment_tree = build_segment_tree(nums)

    def update(self, index, val):
        num_len = len(self.nums)
        index += num_len
        self.segment_tree[index] = val
        while index > 0:
            left = index
            right = index
            if left % 2 == 0:
                right += 1
            else:
                left -= 1
            self.segment_tree[index // 2] = (self.segment_tree[left]
                                             + self.segment_tree[right])
            index = index // 2



    def sumRange(self, left, right):
        num_len = len(self.nums)
        left += num_len
        right += num_len
        sum_r = 0
        while left <= right:
            if left % 2:
                sum_r += self.segment_tree[left]
                left += 1
            if right % 2 == 0:
                sum_r += self.segment_tree[right]
                right -= 1
            left //= 2
            right //= 2
        return sum_r

nums = [1, 3, 5]
na = NumArray(nums)
