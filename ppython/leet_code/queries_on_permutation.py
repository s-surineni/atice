class Fenwick:
    def __init__(self, n):
        sz = 1
        while sz <= n:
            sz *= 2
        self.size = sz
        self.data = [0] * sz

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i < self.size:
            self.data[i] += x
            i += i & -i


class Solution2(object):
    def processQueries(self, queries, n):
        fenw = Fenwick(2 * n)
        vimap = {}
        for idx in range(1, n + 1):
            fenw.add(idx + n, 1)
            vimap[idx] = idx + n
        cur = n

        ans = []
        for qu in queries:
            idx = vimap.pop(qu)
            rank = fenw.sum(idx - 1)
            ans.append(rank)

            vimap[qu] = cur
            fenw.add(idx, -1)
            fenw.add(cur, 1)
            cur -= 1
        return ans


print(Solution2().processQueries([3, 1, 2, 1], 5))
