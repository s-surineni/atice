from functools import lru_cache
from sys import setrecursionlimit as srl
srl(10**6)


class Solution(object):
    def minimumDistance(self, word):
        A = [list("ABCDEF"), list("GHIJKL"), list("MNOPQR"), list("STUVWX"), list("YZ    ")]
        R, C = len(A), len(A[0])

        index = {}
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                index[val] = r, c

        def dist(v1, v2):
            if v1 is None or v2 is None:
                return 0

            r1,c1 = index[v1]
            r2,c2 = index[v2]
            return abs(r1-r2) + abs(c1-c2)

        @lru_cache(None)
        def dp(i, v1=None, v2=None):
            if i == len(word):
                return 0

            # move v1 to i
            ans1 = dist(v1, word[i]) + dp(i+1, word[i], v2)
            ans2 = dist(v2, word[i]) + dp(i+1, v1, word[i])
            return min(ans1, ans2)
        return dp(0)
