from heapq import *

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0


md = MedianFinder()
md.addNum(5)
md.addNum(1)
md.addNum(8)
md.addNum(2)

["Mon",
'Tue',
'Wed',
'Thu',
'Fri',
'Sat',
'Sun']
