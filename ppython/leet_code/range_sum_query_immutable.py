class NumArray:
    def __init__(self, nums):
        self.acc = [0]

        # (Better) way to initialize range sum array
        for a_num in nums:
            self.acc += [self.acc[-1] + a_num]

    def sumRange(self, left, right):
        return self.acc[right + 1] - self.acc[left]


na = NumArray([-2, 0, 3, -5, 2, -1])
