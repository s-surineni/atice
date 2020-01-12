class Solution(object):
    def matrixBlockSum(self, A, K):
        R, C = len(A), len(A[0])
        dp = [[0] * (C+1) for _ in xrange(R+1)]

        for r, row in enumerate(A):
            for c, val in enumerate(row):
                dp[r+1][c+1] = val + dp[r][c+1] + dp[r+1][c] - dp[r][c]

        ans = [[0] * C for _ in xrange(R)]
        for r in xrange(R):
            for c in xrange(C):
                r1 = max(0, r - K)
                c1 = max(0, c - K)
                r2 = min(R-1, r + K)
                c2 = min(C-1, c + K)
                val = dp[r2+1][c2+1] - dp[r2+1][c1] - dp[r1][c2+1] + dp[r1][c1]
                ans[r][c] = val
        return ans
