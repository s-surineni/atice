class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        a_num = int(input('Please enter a number: ').strip())

        low = 0
        high = a_num // 2               # because a sqrt can never be greater than num // 2

        while low < high:
            mid = (low + high) // 2

            if mid ** 2 <= a_num < (mid + 1) ** 2:
                break
            elif a_num < mid ** 2:
                high = mid
            else:
                low = mid + 1
            print(low, high)
        print('sqrt of {} is {}'.format(a_num, mid))
