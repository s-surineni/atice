class DSU:
    def __init__(self, N):
        self.par = list(range(N))

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: return False
        self.par[yr] = xr
        return True

class Solution(object):
    def makeConnected(self, n, connections):
        dsu = DSU(n)
        spare = 0
        components = n
        for u, v in connections:
            if not dsu.union(u, v):
                spare += 1
            else:
                components -= 1
        if components == 1:
            return 0
        if spare >= (components - 1):
            return components - 1
        else:
            return -1
