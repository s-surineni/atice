class RecentCounter:

    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:
        self.pings.append(t)
        # print('t', t)
        idx = self.find_pings_3000(0, len(self.pings) - 1, t - 3000)
        # print('idx', idx)
        return len(self.pings) - idx

    def find_pings_3000(self, l, h, val):
        # print('l h val', l, h, val)
        mid = (l + h) // 2
        if l >= h :
            if val < self.pings[l]:
                return l
            else:
                return l + 1
        if self.pings[mid] == val:
            return mid
        if self.pings[mid] < val:
            return self.find_pings_3000(mid + 1, h, val)
        else:
            return self.find_pings_3000(l, mid - 1, val)


# rc = RecentCounter()
# rc.ping(642)
# rc.ping(1849)
# rc.ping(4921)
# rc.ping(5936)
# rc.ping(5957)

# rc = RecentCounter()
# print(rc.ping(431))
# print(rc.ping(837))
# print(rc.ping(3620))
# print(rc.ping(3837))
# print(rc.ping(3888))

rc = RecentCounter()
print(rc.ping(1))
print(rc.ping(100))
print(rc.ping(3001))
print(rc.ping(3002))

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
