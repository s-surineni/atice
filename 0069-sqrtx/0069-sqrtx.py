class Solution:
    def mySqrt(self, num):
        left, right = 0, num
        res = 0

        while left <= right:
            mid = left + ((right - left ) // 2)
            if mid * mid > num:
                right = mid - 1
            elif mid * mid < num:
                left = mid + 1
                res = mid
            else:
                return mid
        return res